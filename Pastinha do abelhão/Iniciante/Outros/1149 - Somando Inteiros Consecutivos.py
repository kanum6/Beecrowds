lista = [int(x) for x in input().split()]
a = lista[0]
n = lista[-1]
som = 0
for i in range (n):
    som += a + i
    
print (som)