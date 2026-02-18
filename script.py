import sys
from textblob import TextBlob

def analisar_sentimento():
    if len(sys.argv) > 1:
        texto = sys.argv[1]
        
        analise = TextBlob(texto)
        polaridade = analise.sentiment.polarity
        
        if polaridade > 0:
            resultado = "POSITIVE 😊"
        elif polaridade < 0:
            resultado = "NEGATIVE 😡"
        else:
            resultado = "NEUTRAL 😐"
            
        print(f"SENTIMENT_RESULT|{resultado}|Score: {polaridade}")
    else:
        print("ERROR|No text provided")

if __name__ == "__main__":
    analisar_sentimento()
