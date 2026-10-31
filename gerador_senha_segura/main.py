import design
import manipulacao

def main():
    design.titulo('GERADOR DE SENHA SEGURA')
    senha = manipulacao.gerador_senha()
    print(f'Senha gerada: {senha}')

if __name__ == "__main__":
    main()