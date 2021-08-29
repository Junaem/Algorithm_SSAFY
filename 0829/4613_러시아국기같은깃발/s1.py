import sys

sys.stdin = open('input.txt')

def clr_to_chg(row, clr, m):
    return m - flag[row].count(clr)

def russia(N, M):
    min_chg = N*M

    for wht in range(N-2):
        whtnum=0
        for i in range(wht+1):
            whtnum += clr_to_chg(i, 'W', M)


        for blu in range(wht+1, N-1):
            blunum = 0
            for i in range(wht+1, blu+1):
                blunum += clr_to_chg(i, 'B', M)

            rednum = 0
            for i in range(blu+1, N):
                rednum += clr_to_chg(i, 'R', M)
            if whtnum + blunum + rednum < min_chg:
                min_chg = whtnum + blunum + rednum
    return min_chg





T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [input() for _ in range(N)]
    print('#{} {}'.format(tc, russia(N,M)))