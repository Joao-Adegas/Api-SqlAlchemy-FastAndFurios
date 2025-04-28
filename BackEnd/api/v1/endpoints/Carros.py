from typing import List
from fastapi import APIRouter,status,Depends,HTTPException,Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from models.Carro_model import CarroModel
from schemas.Carro_schema import CarroSchema
from core.deps import get_session

router = APIRouter()

@router.post("/",status_code=status.HTTP_201_CREATED,response_model=CarroSchema)
async def post_carro(carro:CarroSchema,db:AsyncSession = Depends(get_session)):
    newCar = CarroModel(carro=carro.carro, cor=carro.cor, motor=carro.motor, QuemDirigiu=carro.QuemDirigiu,img=carro.img )
    db.add(newCar)
    await db.commit()
    return newCar

@router.get("/",response_model=List[CarroSchema])
async def get_car(db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CarroModel)
        result = await session.execute(query)
        carros:List[CarroModel] = result.scalars().all()
        return carros

@router.get("/{carroId}",response_model=CarroSchema,status_code=status.HTTP_200_OK)
async def get_car_by_id(carroId:int,db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CarroModel).filter(CarroModel.id == carroId)
        result = await session.execute(query)
        carro =  result.scalar_one_or_none()

        if carro:
            return carro
        else:
            raise HTTPException(detail = 'Curso não encontrado',status_code=status.HTTP_404_NOT_FOUND)
        
@router.put('/{carId}',response_model=CarroSchema,status_code=status.HTTP_202_ACCEPTED)
async def put_car(carId:int,car:CarroSchema,db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CarroModel).filter(CarroModel.id == carId)
        result = await session.execute(query)
        newCar = result.scalar_one_or_none()
        if(newCar):
            newCar.carro = car.carro
            newCar.cor = car.cor
            newCar.motor = car.motor
            newCar.QuemDirigiu = car.QuemDirigiu
            newCar.img = car.img

            await session.commit()
            return newCar
        else:
            raise HTTPException(detail='Carro não encontrado. Por acaso você assistou Velozes e Furiosos??',status_code=status.HTTP_404_NOT_FOUND)
        

@router.delete("/{CariD}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_car(carId:int,db:AsyncSession = Depends(get_session)):
    async with db as session:
        query = select(CarroModel).filter(CarroModel.id == carId)
        result = await session.execute(query)
        car_del = result.scalar_one_or_none()

        if(car_del):
            await session.delete(car_del)
            await session.commit()
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        else:
            raise HTTPException(detail='Carro não encontrado. Por acaso você assistou Velozes e Furiosos??',status_code=status.HTTP_404_NOT_FOUND)
        

