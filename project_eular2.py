def fibonicci(n, li=[], p=1, q=1):

    if p > n:
        return sum(li)

    p, q = p+q, p
    if not q&1:
        li.append(q)
    return fibonicci(n, li, p, q)



for _ in range(int(input().strip())):
    n = int(input().strip())
    print(fibonicci(n, []))

