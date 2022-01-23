nome=str(input("Qual o nome do Funcionado? "))
sal=float(input("Qual o salario do Funcionario? "))
dep=int(input("Qual e a quantidade de dependente? "))

if dep==0:
    sal = sal+(sal*5/100)
else:
    if (dep>=1) and (dep<=3):
        sal = sal +(sal*10/100)
    elif (dep>=4) and (dep<=6):
        sal = sal +(sal*15/100)
    else:
        sal = sal +(sal*18/100)

print("O novo salario de", nome, f"sera de R${sal:.2f}")
