from __init___ import main
from database import *
from function import *
from ilustration import *

def bet_menu(nft):
    limpar_tela()
    fusion_bet_logo()
    print('''-=-=-=-=-=-=-=-=-=- MENU -=-=-=-=-=-=-=-=-=-=-\n(1). Sua conta\n\n(2). Sobre Nós\n\n(3). BET\n\n(4). Mercado Virtual\n\n(5). Sair\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n
        ''')
    
    escolher_opcao = input('Qual opção deseja escolher?:\n-> ')
    if escolher_opcao in bet_menu:
        bet_menu[escolher_opcao](nft)  
    else:
        bet_menu(nft)

bet_menu_opcoes = {
    '1':'corrida1',
    '2':'corrida2',
    '3':'corrida3',
    '4':'corrida4',
    '5':'corrida5',
    '6':voltar_menu
}