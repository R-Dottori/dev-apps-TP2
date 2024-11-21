# Desenvolvimento de Data-Driven Apps com Python - Teste de Performance 2 (TP2)
# Instituto Infnet - Rafael Dottori de Oliveira
# 21/11/2024

## Descrição
Trabalho para a disciplina de Desenvolvimento de Data-Driven Apps com Python.
As capturas de tela e códigos solicitados estão presentes tanto nos arquivos principais (Jupyter Notebook e PDF) quanto individualmente na raiz do projeto

## Instalação e Uso
1 - Criar um novo ambiente virtual, por exemplo: "python -m venv .venv"

2 - Ativar o ambiente: ".venv/Scripts/activate"

3 - Instalar as dependências: "python -m pip install -r requirements.txt"

4 - Para utilizar o LLM Gemini, criar um arquivo ".env" na raiz do projeto contendo a chave da API: "GEMINI_KEY=chave"

5 - Para rodar cada aplicação, utilizamos Uvicorn via terminal: "uvicorn app_fastapi.main:app" ou "uvicorn app_lanchain.main:app"

6 - Para testar métodos HTTP para cada aplicação, utilizamos o HTTPie via terminal. Exemplo: "http POST localhost:8000/traduzir/alemao/ texto='Please, translate this text.' "