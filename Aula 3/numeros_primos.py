def eh_primo(n):
    primo = True  
 
    if n < 2:
        return False
    
    i = 2
    while i < n:
        if n % i == 0:
            primo = False
            break  
        i += 1  
    
    if primo:
        return True
    else:
        return False
   
numero = int(input("Digite um número: "))
 
if eh_primo(numero):
    print(f"{numero} é primo.")
else:
    print(f"{numero} não é primo.")
    