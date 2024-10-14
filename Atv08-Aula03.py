#Atividade 08:
#Média de Notas:
#Desenvolva um programa que solicite as notas dos alunos até
#que o usuário digite -1. Calcule e exiba a média das notas
#inseridas.

nota = int()
soma = 0
contador = 0
while nota >= 0:
    nota = int(input('Digite a nota do aluno:'))
    if nota == -1:
        break
    else:
        soma += nota
        contador += 1
print(soma / contador)