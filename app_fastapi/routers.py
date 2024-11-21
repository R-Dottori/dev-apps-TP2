
from fastapi import APIRouter
from .models import ModeloTexto, ModeloTraducao
from transformers import pipeline

router = APIRouter()


@router.post('/gerar_texto/')
async def gerar_texto(body: ModeloTexto):
    modelo = pipeline('text-generation', model='gpt2')
    resposta = modelo(body.texto)
    return {'resposta': resposta}


@router.post('/traduzir/')
async def traduzir_texto(body: ModeloTraducao):
    modelo = pipeline('translation_en_to_fr', model='Helsinki-NLP/opus-mt-en-fr', max_length=256)
    resposta = modelo(body.texto)
    return {'resposta': resposta}
