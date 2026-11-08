def titulo(txt):
    print('=' * len(txt))
    print(txt)
    print('=' * len(txt))

def valor_e_validacao():
    while True:
        try:
            valor = int(input('Digite o valor do saque: '))
            if not valor % 2 == 0:
                raise ValueError('O valor deve ser par.')
            else:
                return valor
        except ValueError as erro:
            print(f'Digite um número inteiro válido. {erro}')

def analise_cedulas(valor):
    resultado = {}
    cedulas = [100, 50, 20, 10, 5, 2]
    for cedula in cedulas:
        quantidade = valor // cedula
        if quantidade > 0:
            resultado[cedula] = quantidade
            valor = valor % cedula
    return resultado

def main():
    titulo('CONTADOR DE CÉDULAS')
    valor = valor_e_validacao()
    resultado = analise_cedulas(valor)
    print('\nCÉDULAS ENTREGUES\n')
    for cedula, quantidade in resultado.items():
        print(f'{quantidade} de cédulas de R${cedula}')


if __name__ == "__main__":
    main()