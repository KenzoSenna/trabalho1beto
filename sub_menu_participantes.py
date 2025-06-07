from coisas_que_vou_implementar import *

def submenu_participantes():
    opcoes = {
        "1": listar_participantes_por_evento,
        "2": buscar_participante_por_codigo,
        "3": remover_participante,
        "4": atualizar_info_participante,
        "5": remover_duplicatas,
        "6": lambda: None  # voltar
    }
    while True:
        print("\n--- GERENCIAR PARTICIPANTES ---")
        print("1 - Listar participantes por evento")
        print("2 - Buscar participante por código")
        print("3 - Remover participante")
        print("4 - Atualizar informações do participante")
        print("5 - Remover duplicatas")
        print("6 - Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")
        if escolha == "6":
            break
        acao = opcoes.get(escolha)
        if acao:
            acao()
        else:
            print("Opção inválida.")