# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']


lista = []
lista_desfazer = []

while True:
    print('Comandos: listar, desfazer, refazer, sair')
    opcao = input('Digite uma tarefa ou comando: ').strip()

    if opcao == 'sair':
        break

    elif opcao == 'listar':
        if not lista:
            print('Nenhuma tarefa para listar.')
        else:
            print('TAREFAS:')
            for tarefa in lista:
                print(f'\t{tarefa}')
        print()

    elif opcao == 'desfazer':
        if not lista:
            print('Nada para desfazer.')
        else:
            tarefa_removida = lista.pop()
            lista_desfazer.append(tarefa_removida)
            print(f'Tarefa "{tarefa_removida}" desfeita.')
        print()

    elif opcao == 'refazer':
        if not lista_desfazer:
            print('Nada para refazer.')
        else:
            tarefa_refeita = lista_desfazer.pop()
            lista.append(tarefa_refeita)
            print(f'Tarefa "{tarefa_refeita}" refeita.')
        print()

    else:
        lista.append(opcao)
        print(f'Tarefa "{opcao}" adicionada com sucesso!\n')

