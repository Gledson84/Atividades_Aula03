#Professor Luan esse desafio eu só consegui fazer depois de
#pesquisar no ChatGPT pedindo a solução apenas usando a função while.

#3 - Sequência de Fibonacci:
#Faça um programa que use um laço while para exibir os
#primeiros 20 termos da sequência de Fibonacci.

# Inicializa os primeiros termos da sequência de Fibonacci
a, b = 0, 1
contador = 0

# Exibe os primeiros 20 termos da sequência de Fibonacci
while contador < 20:
    print(a)
    # Atualiza os valores para o próximo termo
    a, b = b, a + b
    contador += 1
