import math
a, b, c = [int(x) for x in input().split()]

a = float(a)
b = float(b)
c = float(c)

delta= ((b**2) - 4*a*c)
if delta <= 0:
    print ("Impossivel calcular")
    exit()

x2 = ((-(b) - math.sqrt(delta)) / (2*a))
x1 = ((-(b) + math.sqrt(delta)) / (2*a))

print (f"R1 = {x1:.5f}")
print (f"R2 = {x2:.5f}")
