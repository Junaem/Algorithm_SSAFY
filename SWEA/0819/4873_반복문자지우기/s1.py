import sys

sys.stdin = open('input.txt')


def puyopuyo(st): # 아무리 생각해도 s2가 옳다. s1은 SWEA에 굴복한 거짓된 풀이이다.
    stack = [] # 쌓을 스택
    for c in st:
        if stack and stack[-1] == c: # 스택의 마지막 글자와 현재 글자가 같으면
            stack.pop() #스택의 글자를 뺀다
        else: # 그렇지 않으면 현재 글자를 스택에 쌓는다.
            stack.append(c)
    return stack


T = int(input())
for tc in range(1, T + 1):
    st = input()
    print('#{} {}'.format(tc, puyopuyo(st)))