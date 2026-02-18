import sys
from textblob import TextBlob
from deep_translator import GoogleTranslator

def analisar_sentimento():
    if len(sys.argv) > 1:
        texto_original = sys.argv[1]
        
        try:
            texto_en = GoogleTranslator(source='auto', target='en').translate(texto_original)
            
            analise = TextBlob(texto_en)
            polaridade = analise.sentiment.polarity
            
            if polaridade > 0.1:
                resultado = "POSITIVE 😊"
            elif polaridade < -0.1:
                resultado = "NEGATIVE 😡"
            else:
                resultado = "NEUTRAL 😐"
                
            print(f"ORIGINAL: {texto_original}")
            print(f"TRANSLATED: {texto_en}")
            print(f"SENTIMENT_RESULT|{resultado}|Score: {polaridade}")
            
        except Exception as e:
            print(f"ERROR|Translation failed: {e}")
    else:
        print("ERROR|No text provided")

if __name__ == "__main__":
    analisar_sentimento()
