d, s = [int(x) for x in input().split()]
Tt = s
val = []

for i in range (d):
    mov = int(input())
    Tt += mov
    val += [Tt]

print (min(val))