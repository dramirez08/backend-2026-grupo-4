from fastapi import FastAPI
from app.routers.pelicula_router import router as pelicula_router

app = FastAPI(title="Catálogo de Series y Películas")
app.include_router(pelicula_router)