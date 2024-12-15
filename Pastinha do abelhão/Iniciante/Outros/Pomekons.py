pal = []
res = int(input())
pomekons = 151

for i in range(res):
    res2 = input("")
    pal.append(res2)

lsd = list(set(pal))
pomekons -= len(lsd)

print (f"Falta(m) {pomekons} pomekon(s).")