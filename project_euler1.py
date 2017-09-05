#!/bin/python3

import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    temp_li = [i for i in range(n) if (i%3==0) or (i%5==0)]
    summation = 0
    for i in temp_li:
        summation += i

    print(summation)
