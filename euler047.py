# the function returns all the prime numbers in a number
def distinctPrimeFactor(num):

    if num < 2:
        return []
    mylist = [0]*num

    for i in range(1, num, 2):
        mylist[i] += 1

    for i in range(3, num//2, 2):
        if not mylist[i-1]:
            p = i-1+i
            for j in range(p, num, i):
                mylist[j] += 1

    return mylist

num, k = map(int, input().split())
li = distinctPrimeFactor(num+k)
for i in range(len(li)-k):
    if li[i]==k:
        for r in range(i, i+k):
            if li[r] != k:
                break
        else:
            print(i+1)
