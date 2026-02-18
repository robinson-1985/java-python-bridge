from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from textblob import TextBlob
from deep_translator import GoogleTranslator

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/", response_class=HTMLResponse)
async def home():
    # Retorna o HTML básico que chama o CSS e JS externos
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <link rel="stylesheet" href="/static/style.css">
        <title>IA Analyzer</title>
    </head>
    <body>
        <div class="card">
            <h1>AI Analyzer 🤖</h1>
            <textarea id="textInput" rows="3"></textarea>
            <button onclick="analyze()">Analisar Sentimento</button>
            <div id="result">
                <span id="emoji" class="emoji"></span>
                <strong id="sentiment"></strong>
                <p id="translation"></p>
            </div>
        </div>
        <script src="/static/script.js"></script>
    </body>
    </html>
    """

@app.get("/analyze")
async def analyze_sentiment(text: str = ""):
    text_en = GoogleTranslator(source='auto', target='en').translate(text)
    score = TextBlob(text_en).sentiment.polarity
    status = "POSITIVE" if score > 0.1 else "NEGATIVE" if score < -0.1 else "NEUTRAL"
    return {"translated_text": text_en, "sentiment": status}
