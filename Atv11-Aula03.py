#Atividade 11: Entrada Válida: 
#Crie um programa que solicite 
#ao usuário um número entre 1 e 10. 
#Continue pedindo até que o usuário 
#forneça um valor válido.

numero = 0

while numero <= 1 or numero >= 10:
    numero = int(input("Digite um número inteiro entre 1 e 10: "))
    if numero > 1 and numero < 10:
        print(f'Número: {numero}, está entre 1 e 10.')
    else:
        print(f'Número: {numero}, não está entre 1 e 10.')