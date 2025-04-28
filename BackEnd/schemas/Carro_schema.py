from typing import Optional
from pydantic import BaseModel as SCBaseModel

class CarroSchema(SCBaseModel):
    id: Optional[int] = None
    carro:str 
    cor:str 
    motor:str 
    QuemDirigiu:str
    img:str

class Config:
    orm_mode = True
    