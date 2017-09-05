def numberSpiral(n):
    
    loop = n//2
    i = 0 ;total = 1; p = 1
    while i < loop:
        for _ in range(4):
            p += (2*(i+1))
            total += p
            #print(p)
        if total > (10**9+7):
            total = total%(10**9+7)
        i += 1

    print('sum of the number spiral of %d:' %n, total)

for _ in range(1, 20, 2):
    numberSpiral(_)

numberSpiral(10**5+1)
