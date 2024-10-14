#Professor Luan esse desafio eu só consegui fazer depois de
#pesquisar no ChatGPT pedindo a solução apenas usando a função while.

# Desenvolva um programa que solicite 
# um número ao usuário
#e use um laço while para calcular o 
# fatorial desse número.
# 
# Solicita um número ao usuário
numero = int(input("Digite um número para calcular o fatorial: "))

# Inicializa o fatorial e o contador
fatorial = 1
contador = 1

# Laço while para calcular o fatorial
while contador <= numero:
    fatorial *= contador  # Multiplica o fatorial pelo contador atual
    contador += 1         # Incrementa o contador

# Exibe o resultado
print(f"O fatorial de {numero} é {fatorial}.")
