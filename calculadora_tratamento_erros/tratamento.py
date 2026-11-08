def obtendo_variaveis():
    while True:
        try:
            x = float(input('Digite o primeiro número: '))
            y = float(input('Digite o segundo número: '))
            return x, y
        except:
            print('Entrada inválida. Digite apenas números')

def cabecalho():
    print('''
OPERAÇÕES ARITMÉTICAS
(1) Soma
(2) Multiplicação
(3) Divisão
(4) Subtração''')
    while True:
        try:
            opcao_escolhida = int(input('Escolha a opção que deseja: '))
            if not 1 <= opcao_escolhida <= 4:
                raise ValueError('Digite uma opção válida!')
            else: 
                return opcao_escolhida
        except ValueError as erro:
            print(f'Erro: {erro}')