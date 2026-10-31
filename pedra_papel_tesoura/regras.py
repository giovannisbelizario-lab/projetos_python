from random import choice

def pedra_papel_tesoura():
    while True: 
        opcoes = ['pedra', 'papel', 'tesoura']
        computador = choice(opcoes)
        jogador = input('Pedra, Papel ou Tesoura? ').strip().lower()
        if jogador not in opcoes:
            print('Escolha inválida! Tente novamente.')
        else: 
            return jogador, computador
