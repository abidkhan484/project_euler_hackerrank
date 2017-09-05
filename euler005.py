from math import sqrt
from math import floor

# the function returns all the prime numbers in a number
def all_prime_between_a_num(num):

    if num < 2:
        return []
    mylist = [1]*num
    mylist[0] = 0

    for i in range(1, num, 2):
        mylist[i] = 0

    for i in range(3, floor(sqrt(num))+2, 2):
        if mylist[i-1] == 0:
            continue
        p = i-1+i
        for j in range(p, num, i):
            mylist[j] = 0

    li = [2]
    for i in range(num):
        if mylist[i]:
            li.append(i+1)

    return li

def smallestMultiple(num):

    if num < 2:
        return 1

    prime = all_prime_between_a_num(num)
    i = 0; total = 1; y = int(sqrt(num))+1
    while prime[i] < y:
        p = prime[i]
        while p <= num:
            p *= prime[i]
        p //= prime[i]
        total *= p
        i += 1
        
    while i < len(prime):
        total *= prime[i]
        i += 1

    return total

for _ in range(int(input().strip())):
    print(smallestMultiple(int(input().strip())))
