a, b, c = [int(x)  for x in input().split(" ")]
if a > b and a > c:
    print (a, "eh o maior")

elif b > a and b > c:
    print (b, "eh o maior")

elif c > b and c > a:
    print (c, "eh o maior")

else:
    print (a, "eh o maior")