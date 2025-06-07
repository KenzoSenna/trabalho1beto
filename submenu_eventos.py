from coisas_que_vou_implementar import *

def submenu_eventos():
    opcoes = {
        "1": listar_eventos,
        "2": adicionar_novo_evento,
        "3": remover_evento,
        "4": buscar_eventos_por_tema_ou_data,
        "5": listar_eventos_por_tema,
        "6": eventos_de_participante,
        "7": eventos_com_poucos_participantes,
        "8": lambda: None  # voltar
    }
    while True:
        print("\n--- GERENCIAR EVENTOS ---")
        print("1 - Listar todos os eventos")
        print("2 - Adicionar novo evento")
        print("3 - Remover evento")
        print("4 - Buscar eventos por tema ou data")
        print("5 - Listar eventos por tema")
        print("6 - Ver eventos de um participante")
        print("7 - Ver eventos com poucos participantes")
        print("8 - Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")
        if escolha == "8":
            break
        acao = opcoes.get(escolha)
        if acao:
            acao()
        else:
            print("Opção inválida.")