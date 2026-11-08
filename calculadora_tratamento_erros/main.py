import design
import tratamento            

soma = lambda x, y: x + y
multiplica = lambda x, y: x * y
divide = lambda x, y: x / y
subtrai = lambda x, y: x - y


def main():
    design.titulo('CALCULADORA COM TRATAMENTO DE ERROS')
    x, y = tratamento.obtendo_variaveis()
    opcao = tratamento.cabecalho()
    operacoes = {1: soma, 2: multiplica, 3: divide, 4: subtrai}
    while True:
        if opcao == 3 and y == 0:
            print('Operação inválida, o divisor não pode ser zero!')
            x, y = tratamento.obtendo_variaveis()
        else:
            resultado = operacoes[opcao](x, y)
            print(f'O resultado da operação é: {resultado}')
            break


if __name__ == '__main__':
    main()