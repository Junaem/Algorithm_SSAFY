import sys

sys.stdin = open('input.txt')

def rest(a, b, c):
    if a == b:
        return c
    elif a == c:
        return b
    else:
        return a




T = int(input())
for tc in range(1, T+1):
    a, b, c = map(int, input().split())
    print('#{} {}'.format(tc, rest(a,b,c)))