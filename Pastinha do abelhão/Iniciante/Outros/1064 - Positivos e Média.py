med = 0
cont = 0
for i in range (6): 
    x = float(input())
    if x > 0:
        med += x
        cont += 1

    else:
        continue

print (f"{cont} valores positivos")
print (round(med/cont, 1))
