#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    temp = (n-1) // 3
    tmp = (n-1) // 5
    t = (n-1) // 15
    temp = (temp * (temp+1)) // 2
    tmp = (tmp * (tmp+1)) // 2
    t = (t * (t+1)) // 2
    temp *= 3
    tmp *= 5
    t *= 15
    print(temp+tmp-t)
