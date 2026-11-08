import design
import tratamento           

def main():
    design.titulo('JOGO DE ADIVINHAR O NÚMERO')
    numero_aleatorio = tratamento.gerar_numero()
    tratamento.adivinhar_numero(numero_aleatorio)

if __name__ == "__main__":
    main()