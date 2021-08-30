import sys

sys.stdin = open('input.txt')

operators = {'+': 1, '-': 1, '*': 2, '/': 2}

def calc(n):
    st = input()
    huwi = []
    opr = []

    for c in st:
        if c in operators:
            while opr and operators[c] <= operators[opr[-1]]:
                huwi.append(opr.pop())
            opr.append(c)
        else :
            huwi.append(int(c))

    huwi += opr[::-1]
    stack = []

    for i in huwi:
        if i in operators:
            b = stack.pop()
            a = stack.pop()

            if i =='+':
                rst = a+b
            elif i == '-':
                rst = a-b
            elif i =='*':
                rst = a*b
            else :
                rst = a/b
            stack.append(rst)
        else:
            stack.append(i)

    return stack[0]







for tc in range(1, 11):
    N = int(input())
    print('#{} {}'.format(tc, calc(N)))