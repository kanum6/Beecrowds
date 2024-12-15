ent1 = input()
a, b, c = ent1.split(" ")

ent2 = input()
A, B, C = ent2.split(" ")

a = int(a)
b = int(b)
c = float(c)

A = int(A)
B = int(B)
C = float(C)

if b != 1: 
    c = (b * c)

if B != 1: 
    C = (B * C)

print (f"VALOR A PAGAR: R$ {c + C:.2f}")