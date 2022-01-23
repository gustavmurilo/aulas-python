qual_seu_nome = input('Qual seu nome? ')
qual_seu_nome = str(qual_seu_nome)

idade_atual = float(input('Qual sua idade? '))

peso_atual = float(input('Qual seu peso atual? '))

qual_sua_altura = float(input('Qual sua altura? '))

peso_ideal = float (qual_sua_altura * qual_sua_altura)
peso_ideal = peso_atual / peso_ideal 
print(f"Seu IMC é!{peso_ideal:.2f}")

if peso_ideal >= 30.0:
  print('Obesidade')
  
elif peso_ideal >= 24.9:
  print('Sobrepeso')

elif peso_ideal >= 18.5:
  print('Normal')

else:
 print('Magreza')