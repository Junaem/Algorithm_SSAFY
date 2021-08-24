import sys

sys.stdin = open('input.txt')

def restore(N): # 문제에서 요구하는 건 0과 1이 몇 번 바뀌는 지이다.
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