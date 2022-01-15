from cgitb import html
from app.database import session
from app.models import Services
from app.services.get_tables import get_table
from app.services.open_file import open_file
from app.config import settings
from app.models import Groups

path = settings.PATH_FOLDER

services = session.query(Services).order_by(Services.id).all()


def main_groups():

    for i in range(len(services)):
        groups = services[i].groups

        groups_list = get_groups_list(i, groups)

        for n in range(len(groups_list)):
            group_dict = {}
            group_dict['id'] = groups[n]['id']
            group_dict['description'] = groups[n]['group']

            html = open_file('{}/{}.{}.html'.format(path, i + 1, n + 1))

            table = get_table(html)

            group_dict = get_groups_dic(group_dict, table)

            save_in_database(group_dict)

    session.close()


def save_in_database(group_dict):
    try:
        groups_cursor = Groups(
            id=group_dict['id'], description=group_dict['description'], compositions=group_dict['compositions'])
        session.add(groups_cursor)
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()


def get_groups_dic(group_dict, table):
    compositions_list = []
    for row in table.find_all('tr'):
        columns = row.find_all('td')

        try:
            if(columns != []):
                s = {}
                s['id'] = columns[1].text.strip()
                s['description'] = columns[2].text.strip()
                s['unid'] = columns[3].text.strip()
                s['price'] = float((columns[4].text.strip()).replace(
                    '.', '').replace(',', '.'))
                compositions_list.append(s)
        except Exception as e:
            print(e)

        group_dict['compositions'] = compositions_list
    return group_dict


def get_groups_list(i, groups):
    for j in range(len(groups)):
        html_file = open_file('{}/{}.html'.format(path, i + 1))

        table = get_table(html_file)

        groups_list = []

        for row in table.find_all('tr'):
            columns = row.find_all('td')

            try:
                if(columns != []):
                    g = columns[1].text.strip()
                    groups_list.append(g)
            except Exception:
                pass
    return groups_list
