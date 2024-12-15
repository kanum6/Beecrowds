ent = input().split(" ")
a, b, c = map(float, ent)

if (a - b) < c or (a + b) > c:
    print (f"Perimetro = {a + b + c}")

elif a < c or b < c:
    A = (a + b)
    print (f"Area = {A * c / 2}")