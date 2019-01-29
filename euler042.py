from math import sqrt

for _ in range(int(input().strip())):
    t = int(input().strip())
    n = (t*8)+1
    p = sqrt(n)
    d = int(p)
    if p != d:
        print(-1)
        continue
    print((d-1)//2) if (d & 1) else print(-1)
