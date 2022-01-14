from app.services import get_table
from app.config import settings
from app.models import Services
from app.database import session
from app.services.open_file import open_file
from time import time
import uuid

path = settings.PATH_FOLDER


def get_services_list():
    html = open_file(path + '/tabela-seinfra.html')

    table = get_table(html)

    services_list = []
    for row in table.find_all('tr'):

        columns = row.find_all('td')

        try:
            if(columns != []):
                c = columns[1].text.strip()
                services_list.append(c)
        except Exception:
            pass
    return services_list


def get_groups_of_supplies(table):
    group_list = []
    n = 0
    for row in table.find_all('tr'):
        n += 1
        columns = row.find_all('td')

        try:
            if(columns != []):
                g = {}
                g['id'] = str(uuid.uuid3(uuid.NAMESPACE_DNS, str(time())))
                g['group'] = columns[1].text.strip()

                group_list.append(g)
        except Exception as e:
            pass
    return group_list


def get_services_table():
    services_list = get_services_list()

    services_tables = []
    for i in range(len(services_list)):
        p = i + 1

        c = {}
        c['id'] = p
        c['description'] = services_list[i]

        groups_path = "{}/{}.html".format(path, p)

        html = open_file(groups_path)

        table = get_table(html)

        group_list = get_groups_of_supplies(table)

        c['groups'] = group_list
        services_tables.append(c)

    return services_tables


def save_services_in_database(services_tables):
    try:
        for service in services_tables:
            services = Services(id=service.get('id'), description=service.get(
                'description'), groups=service.get('groups'))
            session.add(services)
            session.commit()
    except Exception as e:
        session.rollback()


def main_services():
    services_tables = get_services_table()

    save_services_in_database(services_tables)
