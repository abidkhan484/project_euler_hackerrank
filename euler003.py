from math import sqrt
from math import floor

# the function returns all the prime numbers in a number
def all_prime_between_a_num(num):
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


#the function return all prime factor in a num
def prime_factorization(n):

    prime_factor = []
    li = all_prime_between_a_num(floor(sqrt(n))+1)
    terminate = len(li); j = 0
    while j < terminate:
        if not n%li[j]:
            n //= li[j]
            prime_factor.append(li[j])
        else:
            j += 1
    if n != 1:
        prime_factor.append(n)
    return prime_factor

for _ in range(int(input().strip())):
    pr = prime_factorization(int(input().strip()))
    print(pr[-1])
