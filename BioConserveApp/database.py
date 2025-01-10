from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from urllib.parse import quote_plus
from dotenv import load_dotenv
import os

load_dotenv()

USERNAME = os.environ['DATABASE_USERNAME']
PASSWORD = os.environ['DATABASE_PASSWORD']
escaped_password = quote_plus(PASSWORD)
DB_NAME = os.environ['DATABASE_NAME']
DATABASE_URL = f"mysql+aiomysql://{USERNAME}:{escaped_password}@localhost/{DB_NAME}"


engine = create_async_engine(DATABASE_URL, echo=True)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

async def get_db():
    async with async_session() as session:
        try:
            yield session
        finally:
            await session.close()

