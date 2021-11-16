from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from trylikta_paskaita import Projektas

engine = create_engine('sqlite:///trylika.db')
Session = sessionmaker(bind=engine)
session = Session()

while True:
    pasirinkimas = int(input("""Pasirinkite veiksma:
    1 - perziureti irasa
    2 - sukurti nauja irasa
    3 - atnaujinti irasa
    4 - istrinti irasa"""))

    if pasirinkimas == 1:
        trylika = session.query(Projektas).all()
        print("-----------")
        for projektas in trylika:
            print(projektas)
        print("-----------")

    if pasirinkimas == 2:
        vardas = input("Iveskite projekto varda")
        pavarde = input("Iveskite projekto pavarde")
        gimimo_data = input("Iveskite projekto gimimo data")
        pareigos = input("Iveskite projekto pareigas")
        atlyginimas = input("Iveskite projekto atlyginima")
        projektas = Projektas(vardas, pavarde, gimimo_data, pareigos, atlyginimas)
        session.add(Projektas)
        session.commit()

    if pasirinkimas == 3:
        trylika = session.query(Projektas).all()
        print("-----------")
        for projektas in trylika:
            print(projektas)
        print("-----------")
        keiciamo_id = int(input("Pasirinkite norimo pakeisti projekto ID"))
        keiciamas_projektas = session.query(Projektas).get(keiciamo_id)
        pakeitimas = int(input("Ka norite pakeisti: 1 - varda, 2 - pavarde, 3 - gimimo_data, 4 - pareigas, ")), \
                     int(input("5 - atlyginima"))
