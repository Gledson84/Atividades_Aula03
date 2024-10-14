#Atividade 03:
#Tabuada de um Número:
#Faça um programa que solicite um número ao usuário e use
#um laço while para exibir a tabuada desse número (de 1 a 10).

numero = int(input('Digite um número inteiro: '))
controle = 0
while controle <= 10:
    print(f'{numero} x {controle} = {numero * controle}')
    controle += 1