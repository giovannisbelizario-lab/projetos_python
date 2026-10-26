def limpar_texto(texto):
    acentos = 'áéíóúãõâêô'
    substituicao = {'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ã': 'a', 'â': 'a', 'ê': 'e', 'ô': 'o', 'õ': 'o'}
    for letra in acentos:
        texto = texto.replace(letra, substituicao[letra])
    return texto        

def contar_vogais(texto):
    texto_tratado = limpar_texto(texto)
    contagem = {}
    vogais = 'aeiou'
    for letra in texto_tratado:
        if letra in vogais:
            contagem[letra] = contagem.get(letra, 0) + 1
    return contagem