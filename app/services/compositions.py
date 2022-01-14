from app.models import Compositions, compositions
from app.services import verifY_file_name
from bs4 import BeautifulSoup
from app.database import session
import os
import sys

sys.path.append(os.path.realpath('..'))

path = '/home/enganderson/OneDrive/seinfra-ce/html-seinfra'


def get_html_content(filepath):
    if os.path.isfile(filepath):
        if verifY_file_name(filepath):
            with open(filepath, 'r') as f:
                html = f.read()
    return html


def scrap_composition_content(table):
    code = (table.find_all('tr')[0:2][0].text).replace('\n', '')[0:5]

    idx = (table.find_all('tr')[0:2][0].text).replace('\n', '').find('-')

    description = ((table.find_all('tr')[0:2][0].text).replace(
        '\n', '')[7:]).strip()

    unid = (table.find_all('td')[1].text).replace('Unid: ', "")

    price = float((table.find_all('td')[0].text).replace(
        'Preço Adotado: ', '').replace('.', '').replace(',', '.'))

    composition = {
        'id': code,
        'description': description,
        'unid': unid,
        'price': price
    }

    return composition


def scrap_insumos_content(table):
    supplies_list = []
    for row in table.find_all('tr'):
        columns = row.find_all('td')

        try:
            if(columns != []):
                text = columns[1].text.strip()
                c = {}
                c['id'] = columns[0].text.strip()
                c['description'] = text
                c['unid'] = columns[2].text.strip()
                c['coeficient'] = float(
                    columns[3].text.strip().replace('.', '').replace(',', '.'))
                c['price'] = float(columns[4].text.strip().replace(
                    '.', '').replace(',', '.'))
                supplies_list.append(c)
        except Exception:
            pass
    return supplies_list


def list_the_files_and_scrap_compositions_with_supplies():
    compositions = []
    for filename in os.listdir(path):
        try:
            filepath = os.path.join(path, filename)

            html = get_html_content(filepath)

            soup = BeautifulSoup(html, 'html.parser')

            table = soup.find('table')

            table = soup.find('table')

            composition = scrap_composition_content(table)

            supplies_list = scrap_insumos_content(table)

            composition['data'] = supplies_list

            compositions.append(composition)

        except Exception:
            pass
    return compositions


def save_in_database(compositions):
    try:
        for comp in compositions:

            save_in_table = Compositions(id=comp.get('id'), unid=comp.get('unid'), price=comp.get(
                'price'), description=comp.get('description'), insumos=comp.get('data'))

            session.add(save_in_table)
            session.commit()
    except Exception as e:
        session.rollback()


def main_composition():
    compositions = list_the_files_and_scrap_compositions_with_supplies()

    save_in_database(compositions)
