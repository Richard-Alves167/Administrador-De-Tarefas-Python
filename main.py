from funcoesTarefas import * 
from funcoesAuxiliares import *

tarefas = mock_de_tarefas()
parar_loop = False
while(parar_loop == False):
    menu_lista_tarefas()
    opcao = input_int("\nEscolha uma opção do MENU: ")
    match opcao:
        case 1:
            adicionar_tarefa(tarefas)
        case 2:
            visualisar_lista_de_tarefas(tarefas)
        case 3:
            visualisar_tarefa(tarefas)
        case 4:
            marcar_tarefa_para_concluida(tarefas)
        case 5:
            remover_tarefa(tarefas)
        case 6:
            print("Desligando sistema...")
            parar_loop = True
        case _:
            print("!!! Opção inválida !!!")
print("---------- FIM DO PROGRAMA -----------")
