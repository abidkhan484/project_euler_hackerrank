def findFibo():
    a, b = 0, 1
    i = 2
    fibo = [0] * N
    j = 1
    while len(str(b)) < N-1:
        a, b = b, a + b
        j += 1
        if len(str(b)) == i:
            fibo[i] = j
            i += 1
    return fibo


N = 5001
fibo = findFibo()

for _ in range(int(input().strip())):
    print(fibo[int(input().strip())])
