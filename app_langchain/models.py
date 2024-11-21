
from pydantic import BaseModel


class ModeloPergunta(BaseModel):
    pergunta: str


class ModeloTraducao(BaseModel):
    texto: str
