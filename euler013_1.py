# still there is a bug here and testCase2 isn't accept it

# here len1 and len2 is the length of num1 and num2 respectively
def make_addition(num1, num2, len1, len2):
    len1 -= 1; rem = 0

    for i in range(len2-1, -1, -1):
        var = num1[len1] + num2[i] + rem
        if var > 9:
            num1[len1] = var%10
            rem = var//10
        else:
            num1[len1] = var
            rem = 0
        len1 -= 1
    else:
        if rem:
            var = num1[len1]
            var += rem
            if var > 9:
                num1[len1] = var%10
                num1[len1-1] += var//10
            else:
                num1[len1] = var

    return num1


n = int(input().strip())

num1 = list(map(int, input().strip()))

for _ in range(4):
    num1.insert(0,0)

for _ in range(n-1):
    num2 = [int(p) for p in input().strip()]
    make_addition(num1, num2, 54, len(num2))

i = 0
while not num1[i]:
    i += 1

j = i+10
while i < j:
    print(num1[i], end='')
    i += 1

