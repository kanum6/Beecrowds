N, M = [int(x) for x in input().split()]
Ta = 0

for i in range (M):
    ask = input("")
    if ask == "fechou":
        Ta += 1

    else:
        Ta -= 1

print (Ta + N)