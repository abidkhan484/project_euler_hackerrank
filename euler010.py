from math import sqrt
from math import floor

# the function returns all the prime numbers in a number
def all_prime_between_a_num(num):

    if num < 2:
        return []
    mylist = [1]*num
    mylist[0] = 0

    for i in range(3, num, 2):
        mylist[i] = 0

    for i in range(3, floor(sqrt(num))+2, 2):
        if mylist[i-1] == 0:
            continue
        p = i-1+i
        for j in range(p, num, i):
            mylist[j] = 0

    return mylist


def prime_sum():

    length = 10**6
    prime = all_prime_between_a_num(length)
    summation = []; total = 0
    for i in range(length):
        if prime[i]:
            total += (i+1)
        summation.append(total)
    
    return summation


su = prime_sum()
for _ in range(int(input().strip())):

    print(su[int(input().strip())-1])
