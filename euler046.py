from math import floor
from math import sqrt


def getPrimeNum(num):
    mylist = [1] * num
    mylist[0], mylist[1], mylist[2] = 0, 0, 1

    for i in range(4, num, 2):
        mylist[i] = 0

    iterate = floor(sqrt(num))+2
    for i in range(3, iterate, 2):
        if mylist[i] == 0:
            continue
        p = i+i
        for j in range(p, num, i):
            mylist[j] = 0

    return mylist


max_n = (5 * (10**5)) + 1
prime = getPrimeNum(max_n)
info = [0] * max_n

for i in range(2, max_n-2):
    if prime[i]:
        info[i+2] += 1
        j = i + 8; p = 6
        while (j < max_n):
            info[j] += 1
            p += 4
            j += p

for _ in range(int(input().strip())):
    print(info[int(input().strip())])
