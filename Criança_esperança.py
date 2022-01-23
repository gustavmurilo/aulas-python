print("-----------------------------")
print("      CRIANÇA ESPERANÇA      ")
print("-----------------------------")
print("  Muito obrigado por ajudar  ")
print("      [1] para doar R$10     ") 
print("      [2] para doar R$25     ") 
print("      [3] para doar R$50     ") 
print("      [4] para doar outros valores     ") 
print("      [5] para CANCELAR     ") 

d=int(input(" "))
valor=int
if d==1:
    valor=10
    print(valor)
else:
    if d==2:
        valor=25
        print(valor)
    elif d==3:
        valor=50
        print(valor)
    elif d==4:
        valor=(input("Qual o valor da doação? R$ "))
        print(valor)
    elif d==5:
        valor=0
        print(d)
print("-----------------------------")
print(" SUA DOAÇÃO FOI DE R$", valor)
print("MUITO OBRIGADO!")
print("-----------------------------")