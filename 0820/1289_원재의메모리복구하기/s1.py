import sys

sys.stdin = open('input.txt')

def restore(N):
    cnt = 0
    cur = '0'
    for i in N:
        if i != cur:
            cur = i
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = input()
    print('#{} {}'.format(tc, restore(N)))