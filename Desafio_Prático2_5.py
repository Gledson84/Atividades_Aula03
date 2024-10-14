# import random
# numero_aleatorio = random.randint(1, 100)
# while numero_aleatorio >= 1 and numero_aleatorio <= 100:
#     numero = int(input("Digite um número de 1 a 100 e tente descobrir o número secreto: "))
#     if numero == numero_aleatorio:
#         print("Parabéns, você acertou!")
#         break
#     elif numero < numero_aleatorio:
#         print("O número é maior, continue você consegue")
#     elif numero > numero_aleatorio:
#         print("O número é menor, continue você consegue")

#Com uso de prompt no ChatGPT

# import random
# numero_aleatorio = random.randint(1, 100)
# while numero_aleatorio >= 1 and numero_aleatorio <= 100:
#     numero = int(input("Digite um número de 1 a 100 e tente descobrir o número secreto: "))
#     if numero == numero_aleatorio:
#         print("Parabéns, você acertou!")
#         break
#     elif numero < numero_aleatorio:
#         print("O número é maior, continue você consegue")
#     elif numero > numero_aleatorio:
#         print("O número é menor, continue você consegue") 
        
# incremente a melhoria caso o usuario digite um caractere do tipo string

import random

numero_aleatorio = random.randint(1, 100)

while True:
    entrada = input("Digite um número de 1 a 100 e tente descobrir o número secreto: ")
    
    try:
        numero = int(entrada)
        
        if numero < 1 or numero > 100:
            print("Por favor, digite um número entre 1 e 100.")
            continue
            
        if numero == numero_aleatorio:
            print("Parabéns, você acertou!")
            break
        elif numero < numero_aleatorio:
            print("O número é maior, continue você consegue.")
        else:
            print("O número é menor, continue você consegue.")
    
    except ValueError:
        print("Entrada inválida! Por favor, digite um número inteiro.")
