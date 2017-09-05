# for the bigInteger speciality of python

from math import factorial
def digit_sum(num):
    fact = factorial(num)
    fact = str(fact)
    total = 0
    for i in range(len(fact)):
        total += int(fact[i])

    print(total)

for _ in range(int(input().strip())):
    digit_sum(int(input().strip()))
