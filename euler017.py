# number to words

def checkNumber(num):
    string = ''
    if num//100:
        string += words[num//100] + ' ' + bmt[1]
        num %= 100
    if num < 20:
        if string:
            string += ' '
        string += words[num]
    else:
        if string:
            string += ' '
        string += tenth[num//10]
        num %= 10
        if num:
            if string:
                string += ' '
            string += words[num]

    return string
    
def printNumber():
    num = int(input().strip())
    if not num:
        print('Zero')
        return

    ans = ''
    if num//(10**9):
        ans += checkNumber(num//(10**9)) + ' ' + bmt[4]
        num %= (10**9)
    if num//(10**6):
        if ans:
            ans += ' '
        ans += checkNumber(num//(10**6)) + ' ' + bmt[3]
        num %= (10**6)
    if num//(10**3):
        if ans:
            ans += ' '
        ans += checkNumber(num//(10**3)) + ' ' + bmt[2]
        num %= (10**3)

    if num:
        if ans:
            ans += ' '
        ans += checkNumber(num)

    print(ans)



words = {1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven',
       8:'Eight', 9:'Nine', 10:'Ten', 11:'Eleven', 12:'Twelve', 13:'Thirteen',
       14:'Fourteen', 15:'Fifteen', 16:'Sixteen', 17:'Seventeen', 18:'Eighteen',
       19:'Nineteen'
       }
tenth = {2:'Twenty', 3:'Thirty', 4:'Forty', 5:'Fifty', 6:'Sixty', 7:'Seventy',
         8:'Eighty', 9:'Ninety'
        }
bmt = {1: 'Hundred', 2:'Thousand', 3:'Million', 4:'Billion'}

for _ in range(int(input().strip())):
    printNumber()

