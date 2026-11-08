import os

def adicionar_tarefa(tarefas):
    os.system('cls')
    while True:
        tarefas.append(input('Digite a tarefa que deseja adicionar: '))
        while True:
            opcao = input('Quer continuar? [S/N]').strip().upper()
            if opcao in ('N', 'S'):
                break
            print('Digite S ou N.')
        if opcao == 'N':
            break

def visualizar_tarefas(tarefas):
    os.system('cls')
    if not tarefas:
        print('Nenhuma tarefa foi adicionada!')
    else: 
        for indice, tarefa in enumerate(tarefas):
            print(f'{indice + 1}. {tarefa}')
    input('Digite uma tecla para voltar ao menu principal.')

def remover_tarefa(tarefas):
    os.system('cls')
    if not tarefas:
        print('Não existem tarefas para serem removidas.')
    else:
        while True:
            try:
                opc_remover = int(input('Digite o número da opção que deseja remover: '))
            except ValueError:
                print('Digite um número inteiro.')
                continue
            if not 1 <= opc_remover <= len(tarefas):
                print('Opção inválida.')
            else:
                print(f'A tarefa {tarefas[opc_remover - 1]} foi removida com sucesso!')
                tarefas.pop(opc_remover - 1)
                break
    input('Digite uma tecla para voltar ao menu principal.')