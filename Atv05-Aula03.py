#Atividade 05:
#Contagem até o Número Inserido:
#Crie um programa que solicite um número ao usuário e use
#um laço while para contar de 1 até o número inserido,
#exibindo apenas os números ímpares.

numero = int(input('Digite um número positivo e diferente de zero: '))
contagem = 1
while contagem <= numero:
    print(contagem)
    contagem += 2