import sys

sys.stdin = open('input.txt')

dlt = [[0, 1], [0, -1], [-1, 0], [1, 0]]

def repair(N):
    queue = [[0,0]]
    while queue:
        y, x = queue.pop(0)
        if visited[y][x]:
            continue
        visited[y][x] = True
        cur_sum = time_sum[y][x]
        for d in range(4):
            dy, dx = dlt[d]
            ny, nx = y + dy, x + dx
            if not (0 <= ny < N and 0 <= nx < N):
                continue
            nt_sum = time_sum[ny][nx]
            if nt_sum:
                if cur_sum + battleground[ny][nx] < nt_sum:
                    time_sum[ny][nx] = cur_sum + battleground[ny][nx]
            else:
                time_sum[ny][nx] = cur_sum + battleground[ny][nx]
            queue.append((ny, nx))

    return time_sum[N-1][N-1]



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battleground = [list(map(int, input())) for _ in range(N)]
    time_sum = [[0] * N for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    print('#{} {}'.format(tc, repair(N)))