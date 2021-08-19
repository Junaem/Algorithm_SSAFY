import sys

sys.stdin = open('input.txt')

def check(st):
    stack = [] # 여기에 괄호를 쌓아서 검사할 것이다.

    for c in st:
        if c == '{' or c == '(': # 여는 괄호면 스택에 넣는다.
            stack.append(c)
        elif c == '}': # 닫는 괄호이고
            if stack and stack[-1] == '{': # 스택이 있으면서 마지막 스택이 대응하는 괄호이면
                stack.pop() # 스택의 괄호를 뺀다.
            else:
                return 0 # 실패하면 0을 리턴하여 끝낸다.
        elif c == ')': # ')'에도 똑같이 반복
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                return 0
    if stack: # 마지막에 스택이 남아있으면 실패
        return 0
    else : # 비어있으면 성공
        return 1





T = int(input())
for tc in range(1, T+1):
    st = input()
    print('#{} {}'.format(tc, check(st)))