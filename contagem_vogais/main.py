import design
import tratamento

def main():
    design.titulo('CONTAGEM DE VOGAIS EM UM TEXTO')
    texto = input('Digite seu texto: ').lower()
    contagem = tratamento.contar_vogais(texto)
    print('CONTAGEM DE VOGAIS')
    for vogal, valor in contagem.items():
        print(f'{vogal}: {valor}')
    print(f'O total de vogais é: {sum(contagem.values())}')

if __name__ == "__main__":
    main()