import sys

sys.stdin = open('input.txt')

operators = {'+': 1, '-': 1, '*': 2, '/': 2} # 연산자들을 담아두고, 우선순위를 밸류로 표시한 dict

def calc(n):
    st = input()
    huwi = [] # 후위로 표현한 식
    opr = [] # 후위를 만드는 과정에서 연산자들을 담을 리스트

    for c in st:
        try :
            huwi.append(int(c)) # c가 int면 바로 넣는다.
        except: # int가 아니어서 int(c)가 안되면
            while opr and operators[c] <= operators[opr[-1]]: # opr의 위부터 현재 우선순위보다 높은 걸 만날때 까지
                huwi.append(opr.pop())  # 다 huwi에 옮긴다
            opr.append(c) # c를 opr에 담는다
    while opr : # 위 과정이 끝나고 남아있는 opr을
        huwi.append(opr.pop()) # huwi에 거꾸로 담는다.
    stack = [] # 계산을 실행할 때 쓸 스택

    for i in huwi:
        if i in operators: # 연산자를 만나면
            b = stack.pop() # 숫자 2개를 거꾸로 꺼내어
            a = stack.pop()

            if i =='+': # 연산자에 맞는 연산을 한 뒤
                rst = a+b
            elif i == '-':
                rst = a-b
            elif i =='*':
                rst = a*b
            else :
                rst = a/b
            stack.append(rst) # 스택에 쌓는다
        else:
            stack.append(i) # 아니면 바로 숫자를 스택에 쌓는다.

    return stack[0]


for tc in range(1, 11):
    N = int(input())
    print('#{} {}'.format(tc, calc(N)))