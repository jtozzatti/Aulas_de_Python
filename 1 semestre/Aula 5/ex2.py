with open('meuarquivo.txt', 'r', encoding= 'utf-8') as file:
    conteudo = file.read()
    print (conteudo)


with open('meuarquivo.txt', 'r', encoding= 'utf-8') as file:

    linha1 = file.readline()

    linha2 = file.readline()

    linha3 = file.readline()
    print(linha1)
    print(linha2)
    print(linha3)
