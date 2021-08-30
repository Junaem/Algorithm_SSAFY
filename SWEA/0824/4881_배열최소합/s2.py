import sys

sys.stdin = open('input.txt')

def sqr_min(cnt):
    if cnt == N :
        return 0
    min_sum = 500
    for i in range(N):
        if not used[i]:
            used[i] = True
            n_sum = sqr_min(cnt+1) + sqr[cnt][i]
            used[i] = False
            if n_sum > min_sum:
                continue
            min_sum = n_sum
    return min_sum

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sqr = [list(map(int, input().split())) for _ in range(N)]
    used = [False] * N
    result = 500
    print('#{} {}'.format(tc, sqr_min(0)))