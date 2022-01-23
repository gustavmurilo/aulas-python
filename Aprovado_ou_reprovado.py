print("ESCOLA DO GUSTA")
nota_p = (float(input("Primeria Nota: ")))
nota_s = (float(input("Segunda Nota ")))

nota_final=((nota_p+nota_s)/2)

print("MEDIA: ", nota_final)
if nota_final >= 7:
    print("ALUNO APROVADO")
else:
    if (nota_final >= 5) and (nota_final <=7):
        print("ALUNO EM RECUPERAÇÃO")
    else:
        print("ALUNO REPROVADO")