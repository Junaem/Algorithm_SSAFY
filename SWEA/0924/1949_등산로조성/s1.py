import sys

sys.stdin = open('input.txt')

DY = [1, 0, -1, 0]
DX = [0, 1, 0, -1]

def find_bong(mnt, max_h):
    for y in range(N):
        for x in range(N):
            if mnt[y][x] == max_h:
                bongs.append((y, x))

def trail(y, x, fix, former_height):
    height = mnt[y][x]
    if height >= former_height:
        return 0

    visited[y][x] = True
    longest = 0
    for i in range(4):
        ny, nx = y + DY[i], x + DX[i]
        if not (0 <= ny < N and 0 <= nx < N) or visited[ny][nx] :
            continue

        next_height = mnt[ny][nx]
        just_fixed = False

        if next_height >= height and next_height-fix < height and next_height!=1:
            fix = 0
            just_fixed = True
            mnt[ny][nx] = height - 1

        # 다 하고
        result = trail(ny, nx, fix, height) + 1

        if result > longest:
            longest = result

        if just_fixed:
            mnt[ny][nx] = next_height
            fix = K

    visited[y][x] = False
    return longest


def crt_trail(mnt, bongs, max_h):
    longest = 0
    for bong in bongs:
        y, x = bong[0], bong[1]
        result = trail(y, x, K, 21)
        if longest < result:
            longest = result
    return longest


T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    mnt = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]
    max_h = max(map(max, mnt))
    bongs = []
    find_bong(mnt, max_h)
    crt_trail(mnt, bongs, max_h)
    print('#{} {}'.format(tc, crt_trail(mnt, bongs, max_h)))