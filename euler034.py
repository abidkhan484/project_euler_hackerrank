def makeFactorial(num):
    total = 0; n = num
    while num:
        total += fact[num%10]
        num //= 10

    if not (total%n):
        return n
    
    return 0

fact = [1,1]
# here the loop range <10 bcoz digits are btween 0-9
for p in range(2, 10):
    fact.append(fact[-1]*p)

total=0
for i in range(10,int(input().strip())+1):
    total += makeFactorial(i)

print(total)

'''
import time
from math import factorial

t=time.time()

def makeFactorial(num):
    total = 0; n = num
    while num:
        total += factorial(num%10)
        num //= 10

    if not (total%n):
        return n
    
    return 0

total=0
for i in range(10,100000):
    total += makeFactorial(i)
    
print(time.time()-t)


t=time.time()

def makeFactorial(num):
    total = 0; n = num
    while num:
        total += fact[num%10]
        num //= 10

    if not (total%n):
        return n
    
    return 0

fact = [0,1]
# here the loop range <10 bcoz digits are btween 0-9
for p in range(2, 10):
    fact.append(fact[-1]*p)

total=0
for i in range(10,100000):
    total += makeFactorial(i)
    
print(time.time()-t)
'''
