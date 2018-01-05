# solved. but there's some idea from google
from math import factorial as f

def checkNthTerm():
    
    ar = list('abcdefghijklm')
    term = int(input().strip())-1

    length = 12 # this is  len(ar)-1
    string = ''
    while length:
        spam = f(length)
        egg = term//spam
        if term < spam:
            string += ar.pop(0)
        else:
            egg = term//spam
            string += ar.pop(egg)
            term -= (spam*egg)

        length -= 1

    for item in ar:
        string += item
    print(string)

for _ in range(int(input().strip())):
    checkNthTerm()
