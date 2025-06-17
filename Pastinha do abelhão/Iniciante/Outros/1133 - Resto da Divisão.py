a = int(input())
b = int(input())
if a > b:
    val1 = b
    val2 = a

else:
    val1 = a
    val2 = b

for i in range (val1 + 1, val2):
    if i%5 == 2 or i%5 == 3:
        print (i)