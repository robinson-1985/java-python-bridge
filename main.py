from fastapi import FastAPI
from textblob import TextBlob
from deep_translator import GoogleTranslator

app = FastAPI(title="Sentiment Analysis Bridge")

@app.get("/analyze")
async def analyze_sentiment(text: str = ""):
    if not text:
        return {"error": "No text provided"}

    translated = GoogleTranslator(source='auto', target='en').translate(text)
    
    blob = TextBlob(translated)
    score = blob.sentiment.polarity
    
    status = "POSITIVE" if score > 0.1 else "NEGATIVE" if score < -0.1 else "NEUTRAL"
    
    return {
        "original_text": text,
        "translated_text": translated,
        "sentiment": status,
        "score": round(score, 2)
    }
