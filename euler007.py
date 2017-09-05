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


prime_list = all_prime_between_a_num(110000)

for _ in range(int(input().strip())):
    print(prime_list[int(input().strip())-1])
