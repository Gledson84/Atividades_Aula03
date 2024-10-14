#Atividade 06:
#Soma de Números Positivos:
#Escreva um programa que solicite números ao usuário até
#que ele digite um número negativo, somando apenas os
#números positivos inseridos.

numero = int()
soma = 0
while numero >= 0:
    numero = int(input("Digite um número inteiro:"))
    soma += numero
print(soma + 1)