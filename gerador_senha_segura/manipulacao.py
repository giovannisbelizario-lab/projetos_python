import random

def gerador_senha():
    M = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    m = 'abcdefghijklmnopqrstuvwxyz'
    num = '0123456789'
    char = '!@#$%&'

    senha = [random.choice(M), random.choice(m), random.choice(num), random.choice(char)]
    todos_caracteres = M + m + num + char
    senha.extend(random.choices(todos_caracteres, k=8))
    random.shuffle(senha)
    senha_finalizada = ''.join(senha)
    return senha_finalizada