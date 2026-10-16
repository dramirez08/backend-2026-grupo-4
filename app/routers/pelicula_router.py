from fastapi import APIRouter
from app.services.pelicula_service import PeliculaService

router = APIRouter(prefix="/peliculas", tags=["Películas"])
servicio = PeliculaService()

@router.get("/")
def listar_peliculas():
    return servicio.obtener_todas()