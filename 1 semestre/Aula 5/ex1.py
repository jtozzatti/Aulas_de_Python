#Abri um arquivo para escrita
with open('meuarquivo.txt', 'w', encoding= 'utf-8') as file:
    file.write('Olá, mundo!')

#Abrir um arquivo para leitura e escrita
with open('meuarquivo.txt','r+', encoding= 'utf-8') as file:
    conteudo = file.read()
    file.write('\nEste é um arquivo de texto .')

#Abrir um arquivo para anexo
with open('meuarquivo.txt', 'a', encoding= 'utf-8') as file:
    file.write('\nCriado por <João Victor, vulgo marrom provocante>.')