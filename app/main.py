from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from .db import AsyncSessionLocal
from .models import Session

app = FastAPI()

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session

@app.get("/sessions/")
async def read_sessions(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(Session))
        return result.scalars().all()
    except (Exception) as e:
        return {"error": str(e)}
