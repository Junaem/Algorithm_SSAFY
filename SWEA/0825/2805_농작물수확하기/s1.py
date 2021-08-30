import sys

sys.stdin = open('input.txt')

def harvest(N, farm):
    mid = N // 2
    rst = 0
    for i in range(N):
        for k in range(abs(mid-i), N - abs(mid-i)):
            rst += farm[i][k]
    return rst


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    farm = [list(map(int,input())) for _ in range(N)]
    print('#{} {}'.format(tc, harvest(N, farm)))