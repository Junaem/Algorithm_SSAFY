import sys

sys.stdin = open('input.txt')

def dfs(idx, eng, cnt):
    global g_min

    if eng > g_min:
        return

    if cnt == N-1:
        back = eng + mat[idx][0]
        if back < g_min:
            g_min = back
        return

    for i in range(1, N):
        if not visited[i]:
            visited[i] = True
            dfs(i, eng + mat[idx][i], cnt+1)
            visited[i] = False

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    visited = [False for _ in range(N)]
    g_min = sum(mat[(i+1)%N][i] for i in range(N))
    dfs(0, 0, 0)
    print('#{} {}'.format(tc, g_min))