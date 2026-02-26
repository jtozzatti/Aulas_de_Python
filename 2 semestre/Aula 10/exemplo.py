##Leitura e exibição de arquivo CSV em Python

import csv

caminho_arquivo = 'examplo.csv'

with open(caminho_arquivo, mode='r', newline='', encoding='utf8') as arquivo:
    leito_csv = csv.reader(arquivo)

    matriz = list(leito_csv)
    linhas = len(matriz)
    colunas = len(matriz[0])

    print(f"Linhas: {linhas}, Colunas: {colunas}")

    for i in range(linhas):
        for j in range(colunas):
            print(f"| {matriz[i][j]} |", end="")
        print()  