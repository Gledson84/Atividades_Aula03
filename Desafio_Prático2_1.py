# 1 - Números Pares em um Intervalo:
# Crie um programa que solicite dois números ao usuário,
# representando um intervalo. Use um laço while para exibir
# todos os números pares dentro desse intervalo.
n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
contador = n1
while contador <= n2:
    if contador % 2 == 0:
        print(contador)
    contador += 1
