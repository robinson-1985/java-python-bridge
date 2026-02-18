async function analyze() {
    const textInput = document.getElementById('textInput');
    const text = textInput.value;
    if(!text) return;
    
    const btn = document.querySelector('button');
    btn.innerText = "Analisando...";
    btn.disabled = true;

    try {
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
    } catch (error) {
        alert("Erro ao conectar com a API!");
    } finally {
        btn.innerText = "Analisar Sentimento";
        btn.disabled = false;
    }
}