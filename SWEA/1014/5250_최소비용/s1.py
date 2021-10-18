from collections import deque
import sys

sys.stdin = open('input.txt')

Dy = (1, 0, -1, 0)
Dx = (0, 1, 0, -1)


def start(mat):
    need = [[100000 for _ in range(N)] for _ in range(N)]
    need[0][0] = 0
    q = deque([(0, 0)])
    answer = N**2 * 100000

    while q:
        y, x = q.popleft()
        used = need[y][x]
        now_h = mat[y][x]

        for d in range(4):
            ny, nx = y+Dy[d], x+Dx[d]
            if ny not in range(N) or nx not in range(N):
                continue
            nxt_h = mat[ny][nx]
            eng = nxt_h - now_h +1
            if eng < 1:
                eng = 1
            if used + eng < need[ny][nx]:
                need[ny][nx] = used + eng
                q.append((ny, nx))

    return need[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    print('#{} {}'.format(tc, start(mat)))