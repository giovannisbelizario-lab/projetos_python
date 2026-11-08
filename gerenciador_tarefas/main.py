import os
import design
import opcoes
import funcoes

def main():
    tarefas = []
    while True:
        os.system('cls')
        design.titulo_cabecalho('GERENCIADOR DE TAREFAS')
        opcao = opcoes.escolha()
        if opcao == 1:
            funcoes.adicionar_tarefa(tarefas)
        elif opcao == 2:
            funcoes.visualizar_tarefas(tarefas)
        elif opcao == 3:
            funcoes.remover_tarefa(tarefas)
        else:
            print('Saindo do gerenciador de tarefas. Até mais!!')
            break


if __name__ == "__main__":
    main()