import string

def analise_palavras(texto):
    palavras_longas = []
    for palavra in texto:
        palavra = palavra.strip(string.punctuation)
        if len(palavra) > 10:
            palavras_longas.append(palavra)
    return palavras_longas