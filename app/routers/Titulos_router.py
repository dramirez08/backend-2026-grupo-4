from fastapi import APIRouter, HTTPException, Response, status
from pydantic import BaseModel, Field
from app.services.Titulos_service import TitulosService

router = APIRouter(prefix="/Titulos", tags=["encuentro Titulos"])
service = TitulosService()

class ReseñaBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=100)
    formato: str = Field(..., min_length=1, max_length=50)
    año: int = Field(..., ge = 1888, le=2026)
    director_id: int = Field(..., gt = 0)

@router.get("/")
def list_Titulos():
    return service.obtener_todos()

@router.get("/{t_id}")
def obtain_Titulos(c_id: int):
    response = service.obtener_id(c_id)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Titulos no encontrado"
            )
    return response

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_Titulos(Titulos: ReseñaBase):
    return service.create(Titulos.model_dump())

@router.put("/{t_id}")
def update_Titulos(t_id: int, Titulos: ReseñaBase):
    response = service.update(t_id, Titulos.model_dump())
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Titulos no encontrado"
        )
    return response

@router.delete("/{t_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_titulos(t_id: int):
    response = service.delete(t_id)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contenido no encontrado"
            )
    return Response(status_code=status.HTTP_204_NO_CONTENT)

