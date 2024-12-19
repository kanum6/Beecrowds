n1, n2, n3, n4 = [float(x) for x in input().split()]
med = (n1 * 2 + n2 * 3 + n3 * 4 + n4 * 1) / 10
print (f"Média: {med:.1f}")

if med >= 7:
    print ("Aluno aprovado.")

elif med < 5:
    print ("Aluno reprovado.")

elif med <= 6.9 and med >= 5:
    print ("Aluno em exame.")
    nex = float(input())
    print (f"Nota do exame: {nex:.1f}")
    Mf = (med + nex) / 2
    if Mf >= 5:
        print ("Aluno aprovado.")

    elif Mf <= 4.9:
        print ("Aluno reprovado.")
    
    print (f"Media final: {Mf:.1f}")