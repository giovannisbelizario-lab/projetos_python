def analise_vencedor(jogador, computador):
    if jogador == computador:
        return f'''Computador escolheu: {computador}
        Empate!'''
    elif ((jogador == 'pedra' and computador == 'tesoura') or 
        (jogador == 'tesoura' and computador == 'papel') or
        (jogador == 'papel' and computador == 'pedra')):
        return f'''Computador escolheu: {computador}
        Você Venceu!'''
    else: 
        return f'''Computador escolheu: {computador}
        Você Perdeu!'''