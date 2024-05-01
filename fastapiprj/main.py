from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
        Prestart logic
    """
    await delete_tables()
    print("DB was cleaned")

    await create_tables()
    print("DB is ready")
    yield
    print("Power off")


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)