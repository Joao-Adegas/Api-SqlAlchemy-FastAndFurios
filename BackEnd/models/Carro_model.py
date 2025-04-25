from core.configs import settings
from sqlalchemy import Column,Integer,String

class CarroModel(settings.DBBaseModel):
    __tablename__ = 'Carro'

    id:int = Column(Integer,primary_key = True,autoincrement=True)
    carro:str = Column(String(100))
    cor:str = Column(String(100))
    motor:str = Column(String(100))
    QuemDirigiu:str = Column(String(100))
    
