#Código Inicial
numero = int(input("Digite um número: "))
collatz = abs(numero)
while collatz != 1:
    if collatz % 2 == 0:
        collatz = collatz // 2
        print(collatz)
    else: 
        collatz = collatz * 3 + 1
        print(collatz)
        
        
#Código melhorado por meio de prompt no ChatGPT:
#Prompt inserido:
#numero = int(input("Digite um número: "))
# collatz = abs(numero)
# while collatz != 1:
#     if collatz % 2 == 0:
#         collatz = collatz // 2
#         print(collatz)
#     else: 
#         collatz % 2 != 0
#         collatz = collatz * 3 + 1
#         print(collatz)
#Aplique melhorias caso o usuário informe um caractere que não seja um número.
while True:
    try:
        numero = int(input("Digite um número: "))
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Por favor, digite um número válido.")

collatz = abs(numero)
print(collatz)  # Para mostrar o número inicial

while collatz != 1:
    if collatz % 2 == 0:
        collatz = collatz // 2
    else: 
        collatz = collatz * 3 + 1
    print(collatz)

          
            
    
    
        