import sys

sys.stdin = open('input.txt')

D = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def check(y, x, word, cnt):
    if cnt == 7:
        words.add(word)
        return

    for d in range(4):
        ny, nx = y + D[d][0], x + D[d][1]
        if ny in range(4) and nx in range(4):
            check(ny, nx, word + mat[ny][nx], cnt+1)


T = int(input())
for tc in range(1, T+1):
    mat = [input().split() for _ in range(4)]
    words = set()

    for y in range(4):
        for x in range(4):
            check(y, x, '', 0)
    print('#{} {}'.format(tc, len(words)))