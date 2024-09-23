import os
import platform

def escolha(opcoes, msg):
    escolha = input(msg).lower()
    while not escolha in opcoes:
        #limpar_tela()
        print('\nOpção inválida, tente novamente.\n')
        escolha = input(msg).lower()
    return escolha

def verifica_numero(msg):
    numero = input(msg)
    while not numero.isnumeric() or numero == '':
        print('Por favor, digite algum valor correspondente (números).')
        numero = input(msg)
    else:
        numero = int(numero)
    return numero
        
def nao_vazio(msg):
    while True:
        nao_vazio = input(msg)
        if nao_vazio == '':
            limpar_tela()
            print('\nPor favor, insira algum valor.\n')
        else:
            return nao_vazio

def limpar_tela():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')