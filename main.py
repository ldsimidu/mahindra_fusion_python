from function import *
from database import *
dados_conta = None

def main():
    menu_principal()

def confirma_idade(idade):
    if idade < 18:
        print('Você não tem permissão para entrar neste serviço.\nmotivo: IDADE ')
        voltar_menu()
    
def voltar_menu():
    input('\n\nPressione a tecla ENTER para voltar ao menu!')
    limpar_tela()
    main()

def sua_conta():
    global dados_conta
    if dados_conta is not None:
        imprime_dados_conta(dados_conta)
        voltar_menu()
        return
    
    limpar_tela()
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

def sobre_nos():
    mostrar_resumo()
    voltar_menu()

def market_mf():
    if dados_conta == None:
        print('Você não possui uma conta, crie uma primeiro.')
        voltar_menu()
    else:
        idade = dados_conta['Idade']
        confirma_idade(idade)
        menu_market()

def funcao03():
    print('funcao4')

def funcao05():
    print(dados_conta)


def exibir_nft1(produto):
    limpar_tela()
    produto = produtos['NFT1']['nome']
    print("=-=-=-=-=-=-=-= NFT1 =-=-=-=-=-=-=-=")
    print(f'''
          {produtos['NFT1']['nome'].upper()}\n
    -----------------------------------\n
    ID: {produtos['NFT1']['id']}\n
    Quantidade: {produtos['NFT1']['qtd']}\n
    Equipe: {produtos['NFT1']['equipe']}\n
    Veículo: {produtos['NFT1']['veiculo']}\n
    Piloto: {produtos['NFT1']['piloto']}\n
    Velocidade: {produtos['NFT1']['velocidade']}\n
    Corrida: {produtos['NFT1']['corrida']}\n
    Pista: {produtos['NFT1']['pista']}\n
    Volta: {produtos['NFT1']['volta']}\n
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=''')

    resposta = input("\nDeseja...\n\n1 - Ver informações detalhadas\n\n2 - Ver {}").strip().lower()
    
    if resposta == 's':
        print("\n--- Informações Detalhadas ---")
        print(f"Código: {produtos['NFT1']['codigo']}")
        print(f"Preço Final: {produtos['NFT1']['preco']['final']}")
        print(f"Preço Base: {produtos['NFT1']['preco']['base']}")
        #print(f"Desenho: {produtos['NFT1']['desenho']}")
    else:
        print("Ok! Se precisar de mais informações, é só pedir.")
    


def menu_principal():
    limpar_tela()
    print('''
• ▌ ▄ ·.  ▄▄▄·  ▄ .▄▪   ▐ ▄ ·▄▄▄▄  ▄▄▄   ▄▄▄·     ·▄▄▄▄• ▄▌.▄▄ · ▪         ▐ ▄ 
·██ ▐███▪▐█ ▀█ ██▪▐███ •█▌▐███▪ ██ ▀▄ █·▐█ ▀█     ▐▄▄·█▪██▌▐█ ▀. ██ ▪     •█▌▐█
▐█ ▌▐▌▐█·▄█▀▀█ ██▀▐█▐█·▐█▐▐▌▐█· ▐█▌▐▀▀▄ ▄█▀▀█     ██▪ █▌▐█▌▄▀▀▀█▄▐█· ▄█▀▄ ▐█▐▐▌
██ ██▌▐█▌▐█ ▪▐▌██▌▐▀▐█▌██▐█▌██. ██ ▐█•█▌▐█ ▪▐▌    ██▌.▐█▄█▌▐█▄▪▐█▐█▌▐█▌.▐▌██▐█▌
▀▀  █▪▀▀▀ ▀  ▀ ▀▀▀ ·▀▀▀▀▀ █▪▀▀▀▀▀• .▀  ▀ ▀  ▀     ▀▀▀  ▀▀▀  ▀▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪
''')
    
    print('''-=-=-=-=-=-=-=-=-=- MENU -=-=-=-=-=-=-=-=-=-=-\n(1). Sua conta\n\n(2). Sobre Nós\n\n(3). BET\n\n(4). Mercado Virtual\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n
        ''')
    
    escolher_opcao = input('Qual opção deseja escolher?:\n-> ')
    if escolher_opcao in menu_principal_opcoes:
        menu_principal_opcoes[escolher_opcao]()  
    else:
        menu_principal()
        



def menu_market():
    limpar_tela()
    print('''
·▄▄▄▄• ▄▌.▄▄ · ▪         ▐ ▄     • ▌ ▄ ·.  ▄▄▄· ▄▄▄  ▄ •▄ ▄▄▄ .▄▄▄▄▄
▐▄▄·█▪██▌▐█ ▀. ██ ▪     •█▌▐█    ·██ ▐███▪▐█ ▀█ ▀▄ █·█▌▄▌▪▀▄.▀·•██  
██▪ █▌▐█▌▄▀▀▀█▄▐█· ▄█▀▄ ▐█▐▐▌    ▐█ ▌▐▌▐█·▄█▀▀█ ▐▀▀▄ ▐▀▀▄·▐▀▀▪▄ ▐█.▪
██▌.▐█▄█▌▐█▄▪▐█▐█▌▐█▌.▐▌██▐█▌    ██ ██▌▐█▌▐█ ▪▐▌▐█•█▌▐█.█▌▐█▄▄▌ ▐█▌·
▀▀▀  ▀▀▀  ▀▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪    ▀▀  █▪▀▀▀ ▀  ▀ .▀  ▀·▀  ▀ ▀▀▀  ▀▀▀ 
''')
    print('''
-=-=-=-=-=-=- BEM-VINDO AO FUSION MARKET -=-=-=-=-=-=-\n(1). Sobre\n\n(2). Produtos\n\n(3). Voltar\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n  
        ''')
    
    escolher_opcao = input('Qual opção deseja escolher?:\n-> ')
    if escolher_opcao in menu_market_opcoes:
        menu_market_opcoes[escolher_opcao]()  
    else:
        menu_market()


def produtos_market():
    limpar_tela()
    print('''
·▄▄▄▄• ▄▌.▄▄ · ▪         ▐ ▄     • ▌ ▄ ·.  ▄▄▄· ▄▄▄  ▄ •▄ ▄▄▄ .▄▄▄▄▄
▐▄▄·█▪██▌▐█ ▀. ██ ▪     •█▌▐█    ·██ ▐███▪▐█ ▀█ ▀▄ █·█▌▄▌▪▀▄.▀·•██  
██▪ █▌▐█▌▄▀▀▀█▄▐█· ▄█▀▄ ▐█▐▐▌    ▐█ ▌▐▌▐█·▄█▀▀█ ▐▀▀▄ ▐▀▀▄·▐▀▀▪▄ ▐█.▪
██▌.▐█▄█▌▐█▄▪▐█▐█▌▐█▌.▐▌██▐█▌    ██ ██▌▐█▌▐█ ▪▐▌▐█•█▌▐█.█▌▐█▄▄▌ ▐█▌·
▀▀▀  ▀▀▀  ▀▀▀▀ ▀▀▀ ▀█▄▀▪▀▀ █▪    ▀▀  █▪▀▀▀ ▀  ▀ .▀  ▀·▀  ▀ ▀▀▀  ▀▀▀ 
''')
    print('''
-=-=-=-=-=-=- BEM-VINDO AO FUSION MARKET -=-=-=-=-=-=-\n(1). NFT1\n\n(2). NFT2\n\n(3). NFT3\n\n(4). Voltar\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n  
        ''')
    
    escolher_opcao = input('Qual opção deseja escolher?:\n-> ')
    if escolher_opcao in produtos_market_opcoes:
        produtos_market_opcoes[escolher_opcao](produtos)  
    else:
        produtos_market()


menu_principal_opcoes = {
    '1':sua_conta,
    '2':sobre_nos,
    '3':funcao03,
    '4':market_mf,
    '5':funcao05
}

menu_market_opcoes = {
    '1':'sobre',
    '2':produtos_market,
    '3':main
}

produtos_market_opcoes = {
    '1':exibir_nft1,
    '2':'nft2',
    '3':'ntf3',
    '4':menu_market
}
