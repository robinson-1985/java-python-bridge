from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from textblob import TextBlob
from deep_translator import GoogleTranslator

app = FastAPI(title="AI Sentiment Interface")

@app.get("/", response_class=HTMLResponse)
async def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>IA Sentiment Analyzer</title>
        <style>
            body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; background: #121212; color: white; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
            .card { background: #1e1e1e; padding: 2rem; border-radius: 15px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); width: 400px; text-align: center; border: 1px solid #333; }
            h1 { color: #00dc82; margin-bottom: 1.5rem; }
            textarea { width: 100%; padding: 10px; border-radius: 8px; border: none; background: #2d2d2d; color: white; resize: none; margin-bottom: 1rem; }
            button { background: #00dc82; color: #121212; border: none; padding: 10px 20px; border-radius: 8px; font-weight: bold; cursor: pointer; transition: 0.3s; width: 100%; }
            button:hover { background: #00bb6e; transform: translateY(-2px); }
            #result { margin-top: 1.5rem; padding: 1rem; border-radius: 8px; display: none; background: #262626; }
            .emoji { font-size: 2.5rem; display: block; margin-bottom: 0.5rem; }
        </style>
    </head>
    <body>
        <div class="card">
            <h1>AI Analyzer 🤖</h1>
            <textarea id="textInput" rows="3" placeholder="Digite algo em qualquer língua..."></textarea>
            <button onclick="analyze()">Analisar Sentimento</button>
            <div id="result">
                <span id="emoji" class="emoji"></span>
                <strong id="sentiment"></strong>
                <p id="translation" style="font-size: 0.8rem; color: #888; margin-top: 10px;"></p>
            </div>
        </div>

        <script>
            async def analyze() {
                const text = document.getElementById('textInput').value;
                if(!text) return;
                
                const response = await fetch(`/analyze?text=${encodeURIComponent(text)}`);
                const data = await response.json();
                
                const resultDiv = document.getElementById('result');
                const emojiSpan = document.getElementById('emoji');
                const sentimentSpan = document.getElementById('sentiment');
                const transSpan = document.getElementById('translation');

                resultDiv.style.display = 'block';
                sentimentSpan.innerText = data.sentiment;
                transSpan.innerText = "Tradução: " + data.translated_text;

                if(data.sentiment === 'POSITIVE') {
                    emojiSpan.innerText = '😊';
                    sentimentSpan.style.color = '#00dc82';
                } else if(data.sentiment === 'NEGATIVE') {
                    emojiSpan.innerText = '😡';
                    sentimentSpan.style.color = '#ff4b4b';
                } else {
                    emojiSpan.innerText = '😐';
                    sentimentSpan.style.color = '#ffd43b';
                }
            }
        </script>
    </body>
    </html>
    """

@app.get("/analyze")
async def analyze_sentiment(text: str = ""):
    text_en = GoogleTranslator(source='auto', target='en').translate(text)
    score = TextBlob(text_en).sentiment.polarity
    status = "POSITIVE" if score > 0.1 else "NEGATIVE" if score < -0.1 else "NEUTRAL"
    return {"original_text": text, "translated_text": text_en, "sentiment": status, "score": score}
