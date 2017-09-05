def digit_sum(num):

    num = str(num); total = 0
    for i in range(len(num)):
        total += int(num[i])

    return total

for _ in range(int(input().strip())):
    p = 2**(int(input().strip()))
    print(digit_sum(p))
