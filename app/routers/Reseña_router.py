from fastapi import APIRouter, HTTPException, Response, status
from pydantic import BaseModel, Field
from app.services.Reseña_service import ReseñaService

router = APIRouter(prefix="/Reseña", tags=["Reseña del usuario"])
service = ReseñaService()

class ReseñaBase(BaseModel):
    Titulo_id: str = Field(..., gt= 0)
    Comentario: str = Field(..., min_length = 1, max_length = 500)
    Calificacion: int = Field(..., ge = 1.0, le = 5.0)

@router.get("/")
def list_Reseñas():
    return service.obtener_todos()

@router.get("/{r_id}")
def obtain_Reseña(c_id: int):
    response = service.obtener_id(c_id)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Reseña no encontrada"
            )
    return response

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_Reseñas(Titulos: ReseñaBase):
    return service.create(Titulos.model_dump())

@router.put("/{r_id}")
def update_Reseñas(r_id: int, Titulos: ReseñaBase):
    response = service.update(r_id, Titulos.model_dump())
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Reseña no encontrada"
        )
    return response

@router.delete("/{r_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_Reseña(r_id: int):
    response = service.delete(r_id)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail= "Reseña no encontrada"
            )
    return Response(status_code=status.HTTP_204_NO_CONTENT)