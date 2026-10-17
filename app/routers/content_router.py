from fastapi import APIRouter, HTTPException, Response, status
from pydantic import BaseModel, Field
from app.services.content_service import ContentService

router = APIRouter(prefix="/content", tags=["audiovisual content"])
service = ContentService()

class ContentBase(BaseModel):
    titulo: str = Field(..., min_length=1, max_length=100)
    formato: str = Field(..., min_length=1, max_length=50)
    año: int = Field(..., ge=1888, le=2100)

@router.get("/")
def list_content():
    return service.obtener_todos()

@router.get("/{c_id}")
def obtain_content(c_id: int):
    response = service.obtener_por_id(c_id)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contenido no encontrado"
            )
    return response

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_content(content: ContentBase):
    return service.create(content.model_dump())

@router.put("/{c_id}")
def update_content(c_id: int, content: ContentBase):
    response = service.update(c_id, content.model_dump())
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contenido no encontrado"
        )
    return response

@router.delete("/{c_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_content(c_id: int):
    response = service.delete(c_id)
    if not response:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contenido no encontrado"
            )
    return Response(status_code=status.HTTP_204_NO_CONTENT)