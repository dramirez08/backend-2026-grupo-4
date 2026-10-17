from fastapi import FastAPI
from app.routers.content_router import router as content_router

app = FastAPI(title="API Catálogo de Contenidos")

app.include_router(content_router)