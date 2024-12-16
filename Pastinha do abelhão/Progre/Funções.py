AAA = int(input())
for i in range (AAA):
    x, y = [int(x) for x in input().split()]
    R = (3*x)**2 + y**2
    B = 2*(x**2) + (5*y)**2
    C = (-100)*x + y**3
    nums = [R, B, C]
    if max(nums) == R:
        print ("Rafael ganhou")

    elif max(nums) == B:
        print ("Beto ganhou")

    elif max(nums) == C:
        print ("Carlos ganhou")