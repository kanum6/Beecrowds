x, y = [int(a) for a in input().split()]
teodeioluizfelipe = 1
for c in range(0, y):
    if (teodeioluizfelipe+c)%x == 0:
        print (f"{teodeioluizfelipe + c}")
        continue
    print (teodeioluizfelipe + c, end=(" "))