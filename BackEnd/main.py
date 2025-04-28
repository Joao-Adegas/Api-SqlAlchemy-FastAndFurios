from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.configs import settings
from api.v1.api import api_router

app = FastAPI(title='Carros Api - FastAPI AQL Alchemy')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router,prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app",host="127.0.0.1",port=3000,log_level='info',reload=True)