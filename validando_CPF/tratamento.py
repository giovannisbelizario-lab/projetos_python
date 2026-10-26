def validacao_CPF(cpf):
    while True: 
        if len(cpf) != 11: 
            print('O CPF não contém 11 digitos\n')
            cpf = (input('Digite um cpf válido: '))

        if not cpf.isdigit():
            print('O CPF precisa conter apenas números!\n')
            cpf = (input('Digite um cpf válido: '))
        else:
            return cpf