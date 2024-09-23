from function import *
from database import *

def main():
    menu_principal()
    
def sua_conta():
    criar_conta = escolha(s_n_respostas, 'Vimos que não possui uma conta, deseja criá-la?:\n(s/n)-> ')
    if criar_conta == 'n':
        menu_principal()
    else:
        nome = nao_vazio('Insira seu nome completo:\n-> ')
        idade = verifica_numero('Insira sua idade:\n-> ')
        email = nao_vazio('Insira seu email:\n-> ')
        cpf = verifica_numero('Insira seu CPF:\n-> ')

def funcao02():
    print('funcao2')

def funcao03():
    print('funcao3')

def funcao04():
    print('funcao4')

def funcao05():
    print('funcao5')

menu_opcoes = {
    '1':sua_conta,
    '2':funcao02,
    '3':funcao03,
    '4':funcao04,
    '5':funcao05
}

def menu_principal():
    limpar_tela()
    print('''
.___  ___.      ___       __    __   __  .__   __.  _______  .______          ___          _______  __    __       _______. __    ______   .__   __. 
|   \/   |     /   \     |  |  |  | |  | |  \ |  | |       \ |   _  \        /   \        |   ____||  |  |  |     /       ||  |  /  __  \  |  \ |  | 
|  \  /  |    /  ^  \    |  |__|  | |  | |   \|  | |  .--.  ||  |_)  |      /  ^  \       |  |__   |  |  |  |    |   (----`|  | |  |  |  | |   \|  | 
|  |\/|  |   /  /_\  \   |   __   | |  | |  . `  | |  |  |  ||      /      /  /_\  \      |   __|  |  |  |  |     \   \    |  | |  |  |  | |  . `  | 
|  |  |  |  /  _____  \  |  |  |  | |  | |  |\   | |  '--'  ||  |\  \----./  _____  \     |  |     |  `--'  | .----)   |   |  | |  `--'  | |  |\   | 
|__|  |__| /__/     \__\ |__|  |__| |__| |__| \__| |_______/ | _| `._____/__/     \__\    |__|      \______/  |_______/    |__|  \______/  |__| \__| 
                                                                                                                                    
\n''')
    print('''-=-=-=-=-=-=-=-=-=- MENU -=-=-=-=-=-=-=-=-=-=-\n
        (1). Sua conta\n\n(2). Sobre Nós\n\n(3). BET\n\n(4). Mercado Virtual\n\n(5). Sobre Nós\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n
        ''')
    
    escolher_opcao = input('Qual opção deseja escolher?:\n-> ')
    if escolher_opcao in menu_opcoes:
        menu_opcoes[escolher_opcao]()  
    else:
        menu_principal()
    
    