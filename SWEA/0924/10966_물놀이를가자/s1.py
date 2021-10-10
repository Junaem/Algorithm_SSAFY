import sys
from collections import deque

sys.stdin = open('input.txt')

delta = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def bfs(wy, wx, visited, queue):
    now = 0
    # while now < len(queue):
    while queue:
        a = queue.popleft()
        y, x = a[0], a[1]
        now += 1
        dist_now = visited[y][x]

        for i in range(4):
            ny, nx = y + delta[i][0], x + delta[i][1]
            if not (0 <= ny < N and 0 <= nx < M) or land[ny][nx]=='W' or 0 < visited[ny][nx] < dist_now + 1:
                continue
            if visited[ny][nx] != dist_now +1 :
                queue.append((ny, nx))
            visited[ny][nx] = dist_now + 1





def water(land):
    visited = [[0 for _ in range(M)] for _ in range(N)]
    queue = deque()
    for y in range(N):
        for x in range(M):
            if land[y][x] == 'W':
                queue.append((y, x))
    bfs(y, x, visited, queue)

    cnt = sum(map(sum, visited))

    return cnt


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    land = [input() for _ in range(N)]
    print('#{} {}'.format(tc, water(land)))