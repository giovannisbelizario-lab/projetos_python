def escolha():
    while True:
        try:
            opcao = int(input('Escolha a opcão desejada: '))
        except ValueError:
            print('Digite um número inteiro.')
            continue   
        if not 1 <= opcao <= 4:
            print('Escolha uma opção válida! Tente novamente. ')
        else:
            return opcao