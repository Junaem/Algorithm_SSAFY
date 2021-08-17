import sys

sys.stdin = open('input.txt')

def bingo(st):
    if not st:
        return False
    for i in st:
        if i == '.':
            return False
    return True

def omoc(n):
    li = [input() for _ in range(n)]
    for i in range(n):
        for j in range(n - 4):
            garo = ''
            sero = ''
            for k in range(5):
                garo += li[i][j+k]
                sero += li[j+k][i]

            if bingo(garo):
                return 'YES'
            elif bingo(sero):
                return 'YES'

    for i in range(n):
        for j in range(n):
            diag_l = ''
            diag_r = ''
            for k in range(5):
                if i < n-4 and j < n-4:
                    diag_l += li[i+k][j+k]
                if i > 3 and j < n-4:
                    diag_r += li[i-k][j+k]

            if bingo(diag_l):
                return 'YES'
            elif bingo(diag_r):
                return 'YES'

    return 'NO'


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    print('#{} {}'.format(tc, omoc(n)))