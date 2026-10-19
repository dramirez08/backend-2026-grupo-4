from fastapi import FastAPI
from app.routers.Titulos_router import router as Titulos_router
from app.routers.Reseña_router import router as Reseña_router

app = FastAPI(title="API Catálogo de Contenidos")

app.include_router(Titulos_router)
app.include_router(Reseña_router)