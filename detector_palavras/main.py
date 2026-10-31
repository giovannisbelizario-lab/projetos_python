import design
import analise

def main():
    design.titulo('DETECTOR DE PALAVRAS LONGAS')
    texto = input('Digite um texto: ').split()
    resultado = analise.analise_palavras(texto)
    if resultado: 
        print(f'Palavras longas encontradas: {", ".join(resultado)}.')
    else:
        print('Nenhuma palavra longa foi encontrada no texto.')    


if __name__ == '__main__':
    main()