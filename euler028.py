for _ in range(int(input().strip())):
    i = int(input().strip())//2
    print((((16*i**3)+(30*i**2)+(26*i)+3)//3)%(10**9+7))
