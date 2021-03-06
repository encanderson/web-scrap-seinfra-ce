from app.database import Base, engine
from app.services import main_composition
from app.services import main_services
from app.services import main_groups
from app.services import main_insumos

from app.models import Compositions
from app.models import Services
from app.models import Groups
from app.models import Insumos

Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    resp = input(
        "Qual a opção? 1 (Composições) 2 (Serviços) 3 (Insumos) 4 (Insumos)? ")

    if resp == "1":
        main_composition()
    if resp == '2':
        main_services()
    if resp == '3':
        main_groups()
    if resp == '4':
        main_insumos()
