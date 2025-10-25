from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
load_dotenv()

if ("DATABASE_URL" not in os.environ):
    raise EnvironmentError("DATABASE_URL environment variable not set")

engine = create_async_engine(os.getenv("DATABASE_URL"), future=True, echo=True)
AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
Base = declarative_base()