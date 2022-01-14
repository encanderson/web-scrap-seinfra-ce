from app.database import Base, engine
from app.services import main_composition

from app.models import Compositions

Base.metadata.create_all(bind=engine)

if __name__ == '__main__':
    services = ["Composition", "Services", "Suppllies"]

    resp = input("Qual a opção? 1 (Composições) 2 (Serviços) 3 (Insumos)? ")

    if resp == "1":
        main_composition()
