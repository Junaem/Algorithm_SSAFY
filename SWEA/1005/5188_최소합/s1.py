import sys
from collections import deque

sys.stdin = open('input.txt')
D = ((1, 0), (0, 1))

def bfs(mat, dist):
    q = deque([(0, 0)])
    dist[0][0] = mat[0][0]

    while q:
        y, x = q.popleft()
        now = dist[y][x]

        for d in D:
            ny, nx = y+d[0], x+d[1]

            if ny not in range(N) or nx not in range(N):
                continue

            next = dist[ny][nx]

            if not next or next > now + mat[ny][nx]:
                dist[ny][nx] = now + mat[ny][nx]
                q.append((ny, nx))

    return dist[N-1][N-1]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    dist = [[0 for _ in range(N)] for _ in range(N)]
    print('#{} {}'.format(tc, bfs(mat, dist)))