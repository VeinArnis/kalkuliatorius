from sqlalchemy import Column, Integer, String, Float, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
import datetime

engine = create_engine('sqlite:///trylika.db')
Base = declarative_base()


class Projektas(Base):
    __tablename__ = 'Projektas'
    id = Column(Integer, primary_key=True)
    vardas = Column("Vardas", String)
    pavarde = Column("Pavarde", String)
    gimimo_data = Column("Gimimo Data", String)
    pareigos = Column("Pareigos", String)
    atlyginimas = Column("Atlyginimas", Float)
    pradejo_dirbti = Column("Pradejo Dirbti Nuo", DateTime, default=datetime.datetime.now)

    def __init__(self, vardas, pavarde, gimimo_data, pareigos, atlyginimas):
        self.vardas = vardas
        self.pavarde = pavarde
        self.gimimo_data = gimimo_data
        self.pareigos = pareigos
        self.atlyginimas = atlyginimas

    def __repr__(self):
        return f"{self.id} {self.vardas} {self.pavarde} {self.gimimo_data} {self.pareigos} {self.atlyginimas}  " \
               f"{self.pradejo_dirbti}"


Base.metadata.create_all(engine)
