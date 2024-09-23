from function import *
from database import *

dados_conta = {
    'Nome':'',
    'Idade':'',
    'CPF':'',
    'Email':'',
    'Telefone':''
}

def main():
    menu_principal()

def voltar_menu():
    input('\n\nPressione a tecla ENTER para voltar ao menu!')
    limpar_tela()
    main()

dados_conta = None
def sua_conta():
    global dados_conta
    if dados_conta is not None:
        imprime_dados_conta(dados_conta)
        voltar_menu()
        return
    
    criar_conta = escolha(s_n_respostas, 'Vimos que não possui uma conta, deseja criá-la?:\n(s/n)-> ')
    if criar_conta == 'n':
        menu_principal()
    else:
        while True:
            nome = solicitar_dado('Insira seu nome completo:\n-> ', nao_vazio)
            idade = solicitar_dado('Insira sua idade:\n-> ', verifica_numero)
            cpf = solicitar_dado('Insira seu CPF:\n-> ', verifica_numero)
            email = solicitar_dado('Insira seu email:\n-> ', nao_vazio)
            telefone = solicitar_dado('Insira seu número de telefone:\n-> ', verifica_numero)
            
            dados_conta = {
                'Nome': nome,
                'Idade': idade,
                'CPF': cpf,
                'Email': email,
                'Telefone': telefone
            }
            
            imprime_dados_conta(dados_conta)
            confirma_dados = escolha(s_n_respostas, "Seus dados estão corretos?:\n(s/n)-> ")
            if confirma_dados == 'n':
                print('Por favor, insira seus dados novamente.')
            else:
                print('Sua conta foi criada com sucesso!')
                main()  
                return  

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
    print('''-=-=-=-=-=-=-=-=-=- MENU -=-=-=-=-=-=-=-=-=-=-\n(1). Sua conta\n\n(2). Sobre Nós\n\n(3). BET\n\n(4). Mercado Virtual\n\n(5). Sobre Nós\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n
        ''')
    
    escolher_opcao = input('Qual opção deseja escolher?:\n-> ')
    if escolher_opcao in menu_opcoes:
        menu_opcoes[escolher_opcao]()  
    else:
        menu_principal()
    
    