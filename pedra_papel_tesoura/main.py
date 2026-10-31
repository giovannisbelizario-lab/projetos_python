import design
import regras
import analise

def main():
    design.titulo('PEDRA, PAPEL E TESOURA')
    jogador, computador = regras.pedra_papel_tesoura()
    resultado = analise.analise_vencedor(jogador, computador)
    print(resultado)

if __name__ == "__main__":
    main()