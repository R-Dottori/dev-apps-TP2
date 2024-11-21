
from pydantic import BaseModel


class ModeloTexto(BaseModel):
    texto: str


class ModeloTraducao(BaseModel):
    texto: str
