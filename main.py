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


def exibir_detalhes_nft():
    limpar_tela()
    fusion_market_logo()
    """Exibe os detalhes do NFT selecionado."""
    if nft in produtos:
        detalhes = produtos[nft]
        print(f"ID: {detalhes['id']}")
        print(f"Nome: {detalhes['nome']}")
        print(f"Quantidade: {detalhes['qtd']}")
        print(f"Equipe: {detalhes['equipe']}")
        print(f"Veículo: {detalhes['veiculo']}")
        print(f"Piloto: {detalhes['piloto']}")
        print(f"Velocidade: {detalhes['velocidade']}")
        print(f"Corrida: {detalhes['corrida']}")
        print(f"Pista: {detalhes['pista']}")
        print(f"Volta: {detalhes['volta']}")
    else:
        print('NFT NAO ENCONTRADO')
        nft_voltar()

    
    escolher_opcao = input(f"\nDeseja...----------------------\n\n1) Ver informações detalhadas\n\n2) Ver {produtos[nft]['nome']} em representação gráfica\n\n3) Voltar\n\n-------------------------------\n\n-> ").strip().lower()
    
    if escolher_opcao in nft_opcoes:
        nft_opcoes[escolher_opcao]() 
    else:
        exibir_detalhes_nft(nft)

def nft_voltar(nft):
    input('Pressione a tecla ENTER para retornar')
    limpar_tela()
    exibir_detalhes_nft(nft)

def nft_mais_detalhes(nft):
    limpar_tela()
    detalhes = produtos[nft]
    print(f"\n--- Informações Detalhadas ---\nCódigo: {detalhes['codigo']}\nPreço Final: {detalhes['preco']['final']}\nPreço Base: {detalhes['preco']['base']}\n")
    nft_voltar(nft)

def nft_grap(nft):
    limpar_tela()
    detalhes = produtos[nft]
    print(f"Desenho: {detalhes['desenho']}\n\n")
    nft_voltar(nft)

def menu_principal():
    
    limpar_tela()
    mahindra_fusion_logo()
    
    print('''-=-=-=-=-=-=-=-=-=- MENU -=-=-=-=-=-=-=-=-=-=-\n(1). Sua conta\n\n(2). Sobre Nós\n\n(3). BET\n\n(4). Mercado Virtual\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n
        ''')
    
    escolher_opcao = input('Qual opção deseja escolher?:\n-> ')
    if escolher_opcao in menu_principal_opcoes:
        menu_principal_opcoes[escolher_opcao]()  
    else:
        menu_principal()

def menu_market():
    limpar_tela()
    fusion_market_logo()
    print('''
-=-=-=-=-=-=- BEM-VINDO AO FUSION MARKET -=-=-=-=-=-=-\n(1). Sobre\n\n(2). Produtos\n\n(3). Voltar\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n  
        ''')
    
    escolher_opcao = input('Qual opção deseja escolher?:\n-> ')
    if escolher_opcao in menu_market_opcoes:
        menu_market_opcoes[escolher_opcao]()  
    else:
        menu_market()

def produtos_market():
    limpar_tela()
    fusion_market_logo()

    print('''-=-=-=-=-=-=- BEM-VINDO AO FUSION MARKET -=-=-=-=-=-=-\n(1). NFT1\n(2). NFT2\n(3). NFT3\n(4). Voltar\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n''')
    
    escolher_opcao = input('Qual opção deseja escolher?:\n-> ')
    if escolher_opcao in produtos_market_opcoes:
        produto = f'NFT{escolher_opcao}'
        exibir_detalhes_nft(produto)
    elif escolher_opcao == '4':
        menu_market()
    else:
        produtos_market(nft)


menu_principal_opcoes = {
    '1':sua_conta,
    '2':sobre_nos,
    '3':funcao03,
    '4':market_mf
}

menu_market_opcoes = {
    '1':'sobre',
    '2':produtos_market,
    '3':main
}

produtos_market_opcoes = {
    '1': 'NFT1',
    '2': 'NFT2',
    '3': 'NFT3',
    '4': menu_market
}


nft_opcoes = {
    '1':nft_mais_detalhes,
    '2':nft_grap,
    '3':produtos_market
}