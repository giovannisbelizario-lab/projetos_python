import design
import analise_numeros

def main():
    design.titulo('CALCULANDO GORJETA DO RESTAURANTE')
    valor, gorjeta = analise_numeros.obtencao_dados()
    gorjeta_total, conta_total = analise_numeros.tratamento_resultado(valor, gorjeta)
    print(f'O valor da gorjeta é R${gorjeta_total:.2f}')
    print(f'O valor final da conta com serviço é R${conta_total:.2f}')

if __name__ == "__main__":
    main()