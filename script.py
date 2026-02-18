import sys

def processar():
    # Verifica se o Java passou algum argumento
    if len(sys.argv) > 1:
        texto_recebido = sys.argv[1]
        resultado = f"PYTHON DIZ: Recebi '{texto_recebido.upper()}' e ele tem {len(texto_recebido)} letras."
        print(resultado)
    else:
        print("PYTHON DIZ: Não recebi nenhuma mensagem do Java.")

if __name__ == "__main__":
    processar()
