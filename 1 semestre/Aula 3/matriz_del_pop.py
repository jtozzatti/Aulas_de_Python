matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

del matriz[1]

#imprimindo a matriz apos a remoçao da segunda linha
print("matriz apos a remoçao da segunda linha:")
for linha in matriz:
    print (linha)

#usando 'pop' para remover e obter o elemento na terceira linha
elemento = matriz[0].pop(2)
print("\n Elemento removido:", elemento)

#imprimindo a matriz apos a remoçao do elemento
print("\nMatriz aposa remoçao do elemento:")
for linha in matriz:
    print (linha)

#esse remove a linha desejada
