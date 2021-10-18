import sys

sys.stdin = open('input.txt')

def dfs(node, dist):
    global min_dist
    if dist > min_dist: return
    if node == N:
        min_dist = dist
        return

    for i in range(N+1):
        if tree[node][i] and not visited[i]:
            visited[i] = True
            dfs(i, dist+tree[node][i])
            visited[i] = False

T= int(input())
for tc in range(1, T+1):
    N, E = map(int, input().split())
    tree = [[0 for _ in range(N+1)] for _ in range(N+1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        tree[s][e] = w
    visited = [False for _ in range(N+1)]
    min_dist = 10000000
    dfs(0, 0)
    print('#{} {}'.format(tc, min_dist))