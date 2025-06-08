from sub_menu_estatísticas import *
from sub_menu_participantes import *
from submenu_eventos import *

def menu_principal():
    opcoes = {
        "1": submenu_eventos,
        "2": submenu_participantes,
        "3": submenu_estatisticas,
        "0": sair
    }
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Gerenciar eventos")
        print("2 - Gerenciar participantes")
        print("3 - Relatórios e estatísticas")
        print("0 - Sair")

        escolha = input("Escolha uma opção: ")
        acao = opcoes.get(escolha)
        if acao:
            acao()
        else:
            print("Opção inválida.")

def sair():
    print("Encerrando o sistema.")
    exit()

if __name__ == "__main__":
    menu_principal()
