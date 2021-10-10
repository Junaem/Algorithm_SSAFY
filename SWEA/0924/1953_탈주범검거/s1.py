import sys

sys.stdin = open('input.txt')

DLT = [(0, 1), (1, 0), (0, -1), (-1, 0)] # 우, 하, 좌, 상
PIPES = {
    '0' : (),
    '1' : (0, 1, 2, 3),
    '2' : (3, 1),
    '3' : (0, 2),
    '4' : (0, 3),
    '5' : (0, 1),
    '6' : (2, 1),
    '7' : (2, 3)
}


def BFS(R, C, tunnel, L):
    queue = [(R, C)]
    visited[R][C] = 1
    now = 0
    cnt = 1
    time = 0
    # time < L - 1 and
    while time < L and now < len(queue):
        y, x = queue[now][0], queue[now][1]
        now += 1
        pipe = PIPES[tunnel[y][x]]
        time = visited[y][x]

        for way in pipe:
            ny, nx = y + DLT[way][0], x + DLT[way][1]
            if not (0 <= ny < N and 0 <= nx < M) or 0 <= visited[ny][nx] < time+1:
                continue
            elif (way+2)%4 not in PIPES[tunnel[ny][nx]]:
                continue
            if visited[ny][nx] <= 0 and time < L:
                cnt+=1
            queue.append((ny, nx))
            visited[ny][nx] = time + 1

    return cnt



T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    tunnel = [list(input().split()) for _ in range(N)]
    visited = [[-1]*M for _ in range(N)]
    print('#{} {}'.format(tc, BFS(R, C, tunnel, L)))
