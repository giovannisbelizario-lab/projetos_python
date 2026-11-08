from random import randint

def gerar_numero():
    x = randint(1, 100)
    return x

def adivinhar_numero(numero_aleatorio):
    tentativas = 0
    while True: 
        try:
            numero_usuario = int(input('Tente adivinhar o número entre 1 e 100: '))
            if not 1 <= numero_usuario <= 100:
                raise ValueError('O número escolhido está fora do intervalo')
            
            tentativas += 1
            
            if numero_usuario == numero_aleatorio:
                print(f'Você acertou o número secreto "{numero_aleatorio}" em {tentativas} tentativas!!')
                break
            
            elif numero_usuario <= numero_aleatorio:
                print('Muito baixo! Tente novamente')

            else:
                print('Muito alto! Tente novamente')

        except ValueError as erro:
            print(f'Entrada inválida: {erro}. Tente novamente!')