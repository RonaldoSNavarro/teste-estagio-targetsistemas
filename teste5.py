frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # alternativa utilizando fatiamento
print(inverso)