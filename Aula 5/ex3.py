# 1. Criar e escrever no arquivo
with open('programa.le.letra.txt', 'w', encoding='utf-8') as file:
    file.write("Aqui está um exemplo de texto com várias palavras.\n")
    file.write("Vamos contar quantas palavras esse arquivo tem.")

# 2. Ler o arquivo e contar palavras
with open('programa.le.letra.txt', 'r', encoding='utf-8') as file:
    texto = file.read()  # lê todo o conteúdo

palavras = texto.split()  # separa o texto em palavras, usando espaços e quebras

num_palavras = len(palavras)  # conta quantas palavras existem

print(f"O arquivo tem {num_palavras} palavras.")
