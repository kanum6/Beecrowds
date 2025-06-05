num = int(input())

for i in range(num+1):
    if i == 0:
        continue

    elif i%2 == 0:
        print (f"{i}^2 = {i**2}")