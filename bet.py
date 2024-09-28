#pip install tabulate
#pip install pandas
import random
import pandas as pd 
from tabulate import tabulate 
from database import *
from function import *
from ilustration import *

apostas = {}
apostas_realizadas = {}

def calcular_odds(posicao):
    return round(10.0 - (posicao - 1) * (8.5 / 19), 2)

def exibir_corrida(corrida, nome_corrida):
    limpar_tela()
    random.shuffle(corrida)
    df = pd.DataFrame(corrida)
    df["Posição"] = df.index + 1
    df["Odds"] = df["Posição"].apply(calcular_odds)
    df = df[["Posição", "Nome", "Equipe", "Odds"]]
    print(tabulate(df, headers='keys', tablefmt='grid', showindex=False))
    
    if nome_corrida in apostas_realizadas:
        print(f"Você já apostou em {nome_corrida}. Não é possível apostar novamente.\n")
    else:
        while True:
            aposta = input("Em quem deseja apostar? (Informe a posição):\n-> ")
            if not aposta.isdigit() or int(aposta) < 1 or int(aposta) > len(corrida):
                print('Insira uma posição válida.')
            else:
                aposta = int(aposta) - 1
                break

        while True:
            valor_aposta = input("Quanto deseja apostar?\n-> R$ ")
            try:
                valor_aposta = float(valor_aposta)
                if valor_aposta <= 0:
                    print('Insira um valor positivo.')
                else:
                    break
            except ValueError:
                print('Insira um valor numérico válido.')
        
        odds = calcular_odds(aposta + 1)
        apostas[nome_corrida] = {
            "Corredor": corrida[aposta],
            "Valor": valor_aposta,
            "Odds": odds
        }
        apostas_realizadas[nome_corrida] = True
        print(f"Você apostou R$ {valor_aposta:.2f} no {apostas[nome_corrida]['Corredor']['Nome']} da {apostas[nome_corrida]['Corredor']['Equipe']}.\n")


def mostrar_resultados(nft):
    limpar_tela()
    if not apostas:
        print("Nenhuma aposta foi realizada.\n")
        voltar_bet(nft)
        return
    for corrida, aposta_info in apostas.items():
        print(f"\nResultados de {corrida}:")
        posicao_final = random.randint(1, 20)
        print(f"{aposta_info['Corredor']['Nome']} da {aposta_info['Corredor']['Equipe']} ficou na posição {posicao_final}.\n")
        if posicao_final <= 3:
            ganho = aposta_info['Valor'] * aposta_info['Odds']
            print(f"Parabéns! Você ganhou! Lucro: R$ {ganho - aposta_info['Valor']:.2f} (Total: R$ {ganho:.2f})\n")
        else:
            print(f"Você perdeu a aposta de R$ {aposta_info['Valor']:.2f}. Tente novamente!\n")
    voltar_bet(nft)

def corrida1(nft):
    exibir_corrida(corridas["Corrida 1"], "Corrida 1")
    voltar_bet(nft)

def corrida2(nft):
    exibir_corrida(corridas["Corrida 2"], "Corrida 2")
    voltar_bet(nft)

def corrida3(nft):
    exibir_corrida(corridas["Corrida 3"], "Corrida 3")
    voltar_bet(nft)

def corrida4(nft):
    exibir_corrida(corridas["Corrida 4"], "Corrida 4")
    voltar_bet(nft)

def corrida5(nft):
    exibir_corrida(corridas["Corrida 5"], "Corrida 5")
    voltar_bet(nft)


def voltar_bet(nft):
    input('\n\nPressione a tecla ENTER para voltar ao menu!')
    limpar_tela()
    bet_menu(nft)

def bet_menu(nft):
    from main import menu_principal
    limpar_tela()
    fusion_bet_logo()
    print('''-=-=-=-=-=-=-=-=-=- CORRIDAS -=-=-=-=-=-=-=-=-=-=-\n\n(1). São Paulo E-Prix | 25 de Outubro\n\n(2). Monaco E-Prix | 6 de Dezembro\n\n(3). Nova Iorque E-Prix | 30 de Outurbro\n\n(4). Berlin E-Prix | 22 de Novembro\n\n(5). Londres E-Prix | 22 de Dezembro\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n(6). Mostrar Resultados\n\n(7). Voltar\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n''')
    escolher_opcao = input('Qual opção deseja escolher?:\n-> ')
    if escolher_opcao == '7':  
        menu_principal(nft)
    elif escolher_opcao in bet_menu_opcoes:  
        bet_menu_opcoes[escolher_opcao](nft)
    else:
        bet_menu(nft)

bet_menu_opcoes = {
    '1': corrida1,
    '2': corrida2,
    '3': corrida3,
    '4': corrida4,
    '5': corrida5,
    '6': mostrar_resultados
}
