import sys

sys.stdin = open('input.txt')

dlt = [[0, 1], [0, -1], [-1, 0], [1, 0]]

def repair(y, x, cur_time, N):
    global min_time
    for d in range(4):
        dy, dx = dlt[d]
        ny, nx = y + dy, x + dx
        if not (0 <= ny < N and 0 <= nx < N) or visited[ny][nx]:
            continue
        sum_time = cur_time + battleground[ny][nx]
        if sum_time > min_time:
            continue
        if ny == N-1 and nx == N-1:
            if sum_time < min_time:
                min_time = sum_time
            return
        visited[ny][nx] = True
        repair(ny, nx, sum_time, N)
        visited[ny][nx] = False


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    battleground = [list(map(int, input())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    min_time = 90000
    repair(0, 0, 0, N)
    print('#{} {}'.format(tc, min_time))