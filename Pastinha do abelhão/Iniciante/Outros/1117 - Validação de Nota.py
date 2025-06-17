cont = 0
med = 0
while cont != 2:
    a = float(input())
    if a >= 0 and a <= 10:
        med += a
        cont += 1

    else:
        print ("nota invalida")

print (f"media = {med/2:.2f}")