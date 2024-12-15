N = int(input())
lista = list(map(int, input().split()))
a = min(lista)
b = lista.index(a)

print ("Menor valor:", a)
print ("Posicao:", b)