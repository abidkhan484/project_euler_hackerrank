def sumSqrDiff(n):

    print((((n*(n+1))//2)**2)-((n*(n+1)*(2*n+1))//6))

for _ in range(int(input().strip())):
    sumSqrDiff(int(input().strip()))
