## Leitura e exibição de arquivo CSV em Python

import csv

caminho_arquivo = 'exemplo.csv'

with open(caminho_arquivo, mode='r', newline='', encoding='utf8') as arquivo:
    leito_csv = csv.reader(arquivo)

    matriz = list(leito_csv)
    linhas = len(matriz)
    colunas = len(matriz[0])

    print(f"Linhas: {linhas}, Colunas: {colunas}\n")

    # 🔹 Descobrir a largura máxima de cada coluna
    larguras = []

    for j in range(colunas):
        maior = 0
        for i in range(linhas):
            tamanho = len(matriz[i][j])
            if tamanho > maior:
                maior = tamanho
        larguras.append(maior)

    # 🔹 Imprimir tabela alinhada
    for i in range(linhas):
        for j in range(colunas):
            print(f"| {matriz[i][j]:<{larguras[j]}} ", end="")
        print("|")