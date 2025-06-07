from coisas_que_vou_implementar import *

def submenu_estatisticas():
    opcoes = {
        "1": participantes_mais_ativos,
        "2": temas_mais_frequentes,
        "3": taxa_media_participacao,
        "4": lambda: None  # voltar
    }
    while True:
        print("\n--- RELATÓRIOS E ESTATÍSTICAS ---")
        print("1 - Participantes mais ativos")
        print("2 - Temas mais frequentes")
        print("3 - Taxa média de participação por tema")
        print("4 - Voltar ao menu principal")

        escolha = input("Escolha uma opção: ")
        if escolha == "4":
            break
        acao = opcoes.get(escolha)
        if acao:
            acao()
        else:
            print("Opção inválida.")