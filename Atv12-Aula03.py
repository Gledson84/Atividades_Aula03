#Atividade 12: Senha Correta:
#Desenvolva um programa que peça ao usuário 
#para digitar uma senha e continue 
#pedindo até que a senha correta 
#(previamente definida) seja inserida.

senha = ""
senha_definida = "abc123"
while senha != senha_definida:
    senha = input("Digite a senha: ")
    if senha == senha_definida:
        print("Senha Correta")
        break
        
    
    print("Senha Incorreta")