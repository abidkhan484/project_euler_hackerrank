def checking(i, p, arr):

    for j in range(i, p-1, -1):
        if not arr[j]:
            return j+1

def getprod(p,k,arr):

    if p+k>len(arr):
        return p+k, 0
    total = 1
    for i in range(p,p+k):
        total *= arr[i]
    return p+k, total

def solve():
    
    n, k = map(int, input().split())
    arr = list(map(int,input().strip()))

    i=0; total=1
    while i<k:
        total *= arr[i]
        i += 1

    p=0; maxim=total

    while i<n:

        if not total:
            p = checking(i, p, arr)
            i, total = getprod(p,k,arr)
        else:
            total *=arr[i]
            total = total//arr[p]
            i+=1;p+=1

        if total>maxim:
            maxim = total

    print(maxim)

def main():

    for _ in range(int(input().strip())):
        solve()

main()
