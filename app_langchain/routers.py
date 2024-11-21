
from fastapi import APIRouter
from .models import ModeloPergunta, ModeloTraducao
from langchain_community.llms import FakeListLLM
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_huggingface.llms import HuggingFacePipeline
from dotenv import load_dotenv
import os

router = APIRouter()

load_dotenv()

# Instanciamos o modelo fora da função correspondente pois foi a forma de fazê-lo progredir nas respostas da lista
modelo_falso = FakeListLLM(responses=[
                                    'Olá, eu sou um robô!',
                                    'Estou bem, e você?',
                                    'Não sei te dizer...',
                                    'Essa é a última resposta da lista.'
                                    ]
                    )


@router.post('/conversar/')
async def conversa_falsa(body: ModeloPergunta):
    return {'resposta': modelo_falso.invoke(body.pergunta)}


@router.post('/traduzir/frances/')
async def traduzir_gemini(body: ModeloTraducao):
    modelo_traducao_gemini = ChatGoogleGenerativeAI(model='gemini-1.5-flash', api_key=os.getenv('GEMINI_KEY'))
    resposta = ChatPromptTemplate([
        ('system', 'Translate the english texts to french.'),
        ('user', 'Translate the following text: {texto}')
    ])

    return  {'resposta': modelo_traducao_gemini.invoke(resposta.format_messages(texto=body.texto)).content}


@router.post('/traduzir/alemao/')
async def traduzir_huggingface(body: ModeloTraducao):
    modelo_traducao_huggingface = HuggingFacePipeline.from_model_id(model_id='Helsinki-NLP/opus-mt-en-de', task='translation')

    return {'resposta': modelo_traducao_huggingface.invoke(body.texto)}
    
