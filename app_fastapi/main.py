
from fastapi import FastAPI
from .routers import router

app = FastAPI()

app.include_router(router, prefix='/chat')


@app.get('/')
async def raiz():
    return {'mensagem': 'Página raiz'}
