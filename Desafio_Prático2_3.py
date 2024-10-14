# Prompt que utilizei no ChatGPT
# 3 - Soma de Dígitos:
# Escreva um programa que solicite um número ao usuário e use
# um laço while para somar os dígitos do número até que a soma
# seja um único dígito.
#Uuse apenas a função while para resolver o problema
# Aperfeiçoar código caso o usuário informe um número negativo
# aperfeiçoar o código caso o usuário digite um outro caractere que não seja número
# 
# OBS.: Professor Luan me utilizei do enunciado do desafio como prompt e 
# adicionei incrementos para tornar o código melhor, tentei resolver, porém não consegui,
# cheguei até perto da solução, descobri algumas saídas dos operadores "%" e "//" que ainda
# não compreendia, esses desafios são bons, mesmo que não consiga se descobre novo entendimento.
# 
# 
# Solicita um número ao usuário
# Solicita um número ao usuário e valida a entrada
while True:
    entrada = input("Digite um número: ")
    
    # Tenta converter a entrada para um número inteiro
    try:
        numero = int(entrada)
        break  # Sai do laço se a conversão for bem-sucedida
    except ValueError:
        print("Entrada inválida! Por favor, digite um número.")

# Usa o valor absoluto para tratar números negativos
numero = abs(numero)

# Enquanto o número tiver dois ou mais dígitos
while numero >= 10:
    soma = 0
    temp = numero  # Armazena o número temporariamente para a soma dos dígitos
    
    # Soma os dígitos do número
    while temp > 0:
        soma += temp % 10  # Adiciona o último dígito à soma
        temp //= 10        # Remove o último dígito
    
    numero = soma  # Atualiza o número com a soma dos dígitos

# Exibe o resultado
print(f"A soma dos dígitos é: {numero}")
            