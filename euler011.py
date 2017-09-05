arr = [[int(x) for x in input().split()] for j in range(20)]
maxim = -1

# this loop returns right diagonal, right and down multiplication
for k in range(17):
    for i in range(17):
        j = i+4; p = i; total=[1]*4; v=k; u=i
        while p < j:
            total[0] *= arr[k][p]
            total[1] *= arr[p][k]
            total[2] *= arr[v][u]
            total[3] *= arr[u][v]
            p += 1; u+=1; v+=1
        if maxim < max(total):
            maxim = max(total)

# this loop returns the rest of the down and right multiplication
for i in range(17,20):
    for j in range(17):
        p = j; q = j+4; total = [1]*2
        while p < q:
            total[0] *= arr[i][p]
            total[1] *= arr[p][i]
            p += 1
        if maxim < max(total):
            maxim=max(total)

# this loop is used for the left diagonal multiplication
for i in range(17):
    for j in range(19, 2, -1):
        p=j; q=j-4; total=1; v = i
        while p > q:
            total *= arr[v][p]
            p -= 1; v += 1
        if maxim < total:
            maxim = total

print(maxim)
