#Abri um arquivo para escrita
with open('arquivo.txt', 'w', encoding= 'utf-8') as file:
    file.write('Olá, mundo!')

#Abrir um arquivo para leitura e escrita
with open('arquivo.txt','r+') as file:
    conteudo = file.read()
    file.write('\nAdicionando mais conteudo.')

#Abrir um arquivo para anexo
with open('arquivo.txt','a') as file:
    file.write('\nMais uma linha no final do arquivo.')

#encoding= 'utf-8': serve para corrigir os caracteres especiais

##Codigo que geral um texto