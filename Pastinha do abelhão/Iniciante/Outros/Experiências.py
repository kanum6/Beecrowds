N = int(input())

Tc = 0
Tr = 0
Ts = 0
Tt = 0
TTc = 0
TTr = 0
TTs = 0

for i in range(N):
    a, b = input().split()
    a = int(a)
    if b == "C":
        Tc += a
        TTc = Tc
    elif b == "R":
        Tr += a
        TTr = Tr
    elif b == "S":
        Ts += a
        TTs = Ts

    Tt += a
    a = 0

print (f"Total: {Tt} cobaias")
print (f"Total de coelhos: {TTc}")
print (f"Total de ratos: {TTr}")
print (f"Total de sapos: {TTs}")
print (f"Percentual de coelhos: {100 * (Tc/Tt):.2f} %")
print (f"Percentual de ratos: {100 * (Tr/Tt):.2f} %")
print (f"Percentual de sapos: {100 * (Ts/Tt):.2f} %")