from fastapi import FastAPI, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from .database import get_db
app = FastAPI()

@app.get("/")
async def test_db_connection(db: AsyncSession = Depends(get_db)):
    return {"message": "Database connection is working!"}
@app.get("/healthy")
def health_check():
    return {"status": "healthy"}