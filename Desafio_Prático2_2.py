# 2 - Contagem Regressiva com Verificação:
# Faça um programa que use um laço while para fazer uma
# contagem regressiva de um número inserido pelo usuário até 0.
# Durante a contagem, exiba "Número par" para os números
# pares.
numero = int(input('Digite um número: '))
contagem = numero
while contagem >= 0:
    if contagem % 2 == 0:
        print(f'{contagem} - Número par')
    else:
        print(contagem)
    contagem -= 1