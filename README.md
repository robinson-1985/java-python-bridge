# 🌉 Java-Python AI Bridge (Web API Edition)

Este projeto demonstra uma arquitetura de microsserviços onde um cliente **Java** consome uma API de Inteligência Artificial escrita em **Python (FastAPI)** para análise de sentimentos com tradução automática.

![Java](https://img.shields.io/badge/java-%23ED8B00.svg?style=for-the-badge&logo=openjdk&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

## 🚀 Como Funciona
1.  **Java Client:** Envia uma frase (em qualquer língua) via requisição HTTP GET.
2.  **Python API:** Recebe o texto, traduz para o Inglês e utiliza **Processamento de Linguagem Natural (NLP)** para calcular a polaridade do sentimento.
3.  **JSON Response:** A API retorna um objeto JSON com o sentimento (Positivo, Negativo ou Neutro) e o score da análise.

## 🛠️ Tecnologias
- **Java 17+**: HttpClient e codificação URI.
- **Python 3.x**: FastAPI, Uvicorn, TextBlob (IA) e Deep Translator.
- **Ubuntu Linux**: Ambiente de desenvolvimento e execução.

## 📦 Como Executar

### 1. Servidor Python (API)
```bash
cd projeto-hibrido
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload
