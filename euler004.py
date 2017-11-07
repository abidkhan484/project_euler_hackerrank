def checkPalindrome(n):
    n = str(n)
    for i in range(3):
        if n[i] != n[6-i-1]:
            return False
    return True

def largestPalindrome():
    num = int(input().strip())
    for i in range(len(mylist)-1, -1, -1):
        if mylist[i] < num:
            print(mylist[i])
            return

p = 101

ar = []
# here 450 is ((999+101)//2)-100
for i in range(101, 1000):

    t = 100000/p
    if t != int(t):
        t = int(t) + 1
    else:
        t = int(t)

    for j in range(t, 1000):
        ar.append(p*j)
    p += 1


ar = list(set(ar))
ar.sort()

mylist = []
for i in range(len(ar)):
    if checkPalindrome(ar[i]):
        mylist.append(ar[i])

del ar        

for _ in range(int(input().strip())):
    largestPalindrome()


'''
# from the editorial; see the bisect package
# it can be used like binary search


#/usr/bin/python

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from bisect import bisect_left as bl
arr = []
for i in range(999,100,-1):
    for j in range(999,100,-1):
        t = str(i*j)
        if t == t[::-1]:
            arr.append(i*j)
arr.sort()
for _ in range(int(raw_input())):
    i = bl(arr,int(raw_input()))
    print arr[i-1]

'''
