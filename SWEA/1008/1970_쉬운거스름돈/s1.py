import sys

sys.stdin = open('input.txt')

CURR = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

def change(N):
    ans = [0] * 8

    for i in range(8):
        ans[i] = N//CURR[i]
        N %= CURR[i]
    return ans

T = int(input())
for tc in range(1, T+1):
    N = int(input())

    print('#{}'.format(tc))
    print(*change(N))
