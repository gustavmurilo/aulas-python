nome = input("Digite seu nome?  ")
print("Bem-vindo", nome)

ano_estamos = int(input("Em que anos estamos? ",))
print("Entendi, estamos no ano", ano_estamos)
ano_nascimento = int(input("Em que ano você nasceu? "))
print("Entendi, você nasceu no ano", ano_nascimento)

sua_idade = int(ano_estamos-ano_nascimento)
print("A sua idade é" , sua_idade)
if (sua_idade >= 18):
    print("e já tingiu a maioridade.")
else:
    print("#chateado")