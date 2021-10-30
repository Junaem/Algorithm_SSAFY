import sys

sys.stdin = open('input.txt')

DLT =((1, 1), (1, -1), (-1, -1), (-1, 1))

def travel(y, x, p_drc, mcr, start):
    global max_mcr
    len_mcr = len(mcr)
    if (y-1, x+1) == start and len_mcr >2:
        if len_mcr > max_mcr:
            max_mcr = len_mcr
        return

    ran = 2
    if (y, x) == start :
        ran = 1
    for d in range(ran):
        drc = p_drc+d
        if drc > 3: continue

        ny, nx = y+DLT[drc][0], x+DLT[drc][1]
        min_x  = max(start[1] -ny + start[0], 0)

        if ny not in range(start[0], N) or nx not in range(min_x, N): continue
        if street[ny][nx] in mcr: continue

        mcr.append(street[ny][nx])
        travel(ny, nx, drc, mcr, start)
        mcr.pop()



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    street = [list(map(int, input().split())) for _ in range(N)]
    max_mcr = -1
    for i in range(N):
        for j in range(N):
            travel(i, j, 0, [street[i][j]], (i, j))
    print('#{} {}'.format(tc, max_mcr))