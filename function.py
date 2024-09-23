import os
import platform
from database import *

def solicitar_dado(mensagem, funcao_validacao):
    limpar_tela()
    return funcao_validacao(mensagem)

def imprime_dados_conta(dados):
    limpar_tela()
    print("\nDados da Conta:")
    print("-" * 30)
    for chave, valor in dados.items():
        print(f"{chave: <10}: {valor}")
    print("-" * 30)

def mostrar_resumo():
    limpar_tela()
    print(titulo)
    print("\nIntrodução:")
    print(introducao)
    print("\nProblema:")
    print(problema)
    print("\nSolução Proposta:")
    print(solucao)
    print("\n" + objetivos)
    print("\nJustificativa:")
    print(justificativa)
    print("\nConclusão:")
    print(conclusao + '\n\n')
    


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
        limpar_tela()
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