import sys

sys.stdin = open('input.txt')

operators = '+-*/' # 연산자들

def forth(li):
    stack = [] # 계산을 진행할 스택
    for i in li:
        if i in operators: # i가 연산자면
            try:  # 숫자 2개를 거꾸로 꺼내본다.
                b = int(stack.pop())
                a = int(stack.pop())
            except: # 실패하면 에러 출력
                return 'error'
            # 꺼냈다면 연산자에 맞는 연산을 한다.
            if i == '+':
                rslt = a + b
            elif i == '-':
                rslt = a - b
            elif i == '*':
                rslt = a * b
            elif i == '/' :
                rslt = a // b
            stack.append(rslt) # 결과를 스택에 더한다
        elif i == '.': #  '.' 을 만나고 스택이 연산결과 하나만 남아있을 때 출력,
            if len(stack) == 1:   # 이 처리를 안해서 계속 에러가 떴다.
                return stack.pop()
            else: # 아니면 에러
                return 'error'
        elif i.isdigit() : # i가 숫자이면
            stack.append(i) # 스택에 더한다.
        else:
            return 'error'


T = int(input())

for tc in range(1, T+1):
    li = list(input().split())
    print('#{}'.format(tc), forth(li))