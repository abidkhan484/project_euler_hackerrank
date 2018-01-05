def checkTriplet(item):
 
    if item & 1:
        return -1
    item = item >> 1
 
    m = 2; mylist=[]
    while True:
        n = (item/m)-m
        if not (n > 0):
            break
 
        if (n == int(n)) and (n < m):
            n = int(n)
            mylist.append([m,n])
        m += 1
 
    if not mylist:
        return -1
    maxim = -1
    for m, n in mylist:
        x, y, z = ((m**2 - n**2), (2*m*n), (m**2 + n**2))
        if (x*y*z) > maxim:
            a, b, c = x, y, z
            maxim = (x*y*z)
 
    return a, b, c
 
 
triplet = [0]*3001
for item in range(3001):
 
    t = checkTriplet(item)
    if t == -1:
        if not triplet[item]:
            triplet[item] = -1
        continue
 
    a, b, c = t
    if (a*b*c) < triplet[item]:
        continue
    p, q, r = t
    while (a + b + c) < 3001:
        if triplet[a+b+c] < (a*b*c):
            triplet[a+b+c] = (a*b*c)
        a += p; b += q; c += r
 
for _ in range(int(input().strip())):
    print(triplet[int(input().strip())])
 
'''
# another approach; time and memory complexity
# is greater than the previous one
 
from math import sqrt
 
pr = [[] for _ in range(3001)]
for a in range(1, 2000):
    for b in range(a, 2000-a):
        c = sqrt(a**2 + b**2)
        if c == int(c) and (a+b+c) < 3001:
            pr[(a+b+int(c))].append([a,b,int(c)])
 
for _ in range(int(input().strip())):
    tmp = int(input().strip())
    maxim = -1
    for a, b, c in pr[tmp]:
        if (a*b*c) > maxim:
            maxim = a*b*c
    print(maxim)
'''
 
