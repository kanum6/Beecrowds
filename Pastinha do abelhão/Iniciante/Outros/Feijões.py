c1, c2, c3, c4 = [int(x) for x in input().split()]
f = [c1, c2, c3, c4]

for i in f:
    if i == 1:
        print (f.index(i)+1)