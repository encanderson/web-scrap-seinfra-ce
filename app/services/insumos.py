import pandas as pd
from app.database import session
from app.models import Insumos
from app.config import settings

path = settings.PATH_FOLDER

table_excel = pd.read_excel(path + '/seinfra-insumo.xlsx')

table_dict = table_excel.to_dict()


def main_insumos():
    for i in range(len(table_excel)):
        c = {}
        c['id'] = table_dict['id'][i]
        c['description'] = table_dict['description'][i]
        c['unid'] = table_dict['unid'][i]
        c['price'] = table_dict['price'][i]

        insumo = Insumos(
            id=c['id'], description=c['description'], unid=c['unid'], price=c['price'])

        session.add(insumo)
        session.commit()
