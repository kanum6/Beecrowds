sal1 = float(input())
sal2 = sal1

if sal1 >= 0 and sal1 <= 400:
    saln = sal1/100 * 15
    print (f"Novo salario: {saln + sal2:.2f}\nReajuste ganho: {saln:.2f}\nEm percentual: 15 %")

if sal1 >= 400.01 and sal1 <= 800:
    saln = sal1/100 * 12
    print (f"Novo salario: {saln + sal2:.2f}\nReajuste ganho: {saln:.2f}\nEm percentual: 12 %")

if sal1 >= 800.01 and sal1 <= 1200:
    saln = sal1/100 * 10
    print (f"Novo salario: {saln + sal2:.2f}\nReajuste ganho: {saln:.2f}\nEm percentual: 10 %")

if sal1 >= 1200.01 and sal1 <= 2000:
    saln = sal1/100 * 7
    print (f"Novo salario: {saln + sal2:.2f}\nReajuste ganho: {saln:.2f}\nEm percentual: 7 %")

if sal1 > 2000:
    saln = sal1/100 * 4
    print (f"Novo salario: {saln + sal2:.2f}\nReajuste ganho: {saln:.2f}\nEm percentual: 4 %")