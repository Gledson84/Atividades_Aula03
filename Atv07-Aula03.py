#Atividade 07:
#Tabuada com Condicional:
#Faça um programa que solicite um número ao usuário e use
#um laço while para exibir a tabuada desse número (de 1 a 10),
#mas apenas para os resultados que forem múltiplos de 3.

numero = int(input('Digite um número: '))
multiplicador = 3
while multiplicador <= 10:
    print(f'{numero} x {multiplicador} = {numero * multiplicador}')
    multiplicador += 3
    