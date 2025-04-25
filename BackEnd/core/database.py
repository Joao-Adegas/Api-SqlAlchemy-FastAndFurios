from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from core.configs import settings

'''
Session retorna uma classe que abri e fecha a conexão com o banco de dados
'''

engine:AsyncEngine = create_async_engine(settings.DB_URL)

Session: AsyncEngine = sessionmaker(
    autoflush=False,
    autocommit = False,
    expire_on_commit=False,
    class_ = AsyncSession,
    bind=engine
)

