from fastapi import APIRouter

from api.v1.endpoints import carros

api_router = APIRouter()
api_router.include_router(carros.router,prefix='/carros',tags=['carros'])
