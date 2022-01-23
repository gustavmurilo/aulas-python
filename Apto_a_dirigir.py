atual=int(input("Ano Atual (yyyy): "))
nascimento=int(input("Ano de Nascimento (yyyy): "))
anos_hoje=(atual-nascimento)
print("IDADE:", anos_hoje, "Anos")
if anos_hoje >= 18:
    print("APTO A TIRAR A CARTEIRA")
    
