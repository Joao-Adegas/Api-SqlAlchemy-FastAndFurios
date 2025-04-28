from fastapi import APIRouter

from api.v1.endpoints import Carros

api_router = APIRouter()
api_router.include_router(Carros.router,prefix='/carros',tags=['carros'])
