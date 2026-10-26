def obtencao_dados():
    valor_conta = float(input('Digite o valor da conta: R$'))
    gorjeta = float(input('Digite o percentual da gorjeta: '))
    return valor_conta, gorjeta

def tratamento_resultado(x, y):
    gorjeta = x * (y/100)
    total_conta = (x * (1+(y/100)))
    return gorjeta, total_conta