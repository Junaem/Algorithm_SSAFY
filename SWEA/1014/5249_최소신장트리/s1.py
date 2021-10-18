import sys

sys.stdin = open('input.txt')

def dfs(node, depth, eng):
    global min_eng
    if eng > min_eng: return
    if depth == V:
        for i in range(V+1):
            if not visited[i]:
                return
        min_eng = eng
        return
    for next in range(V+1):
        gansun = tree[node][next]
        if gansun:
            tree[node][next] = 0
            tree[next][node] = 0
            visited[next] +=1
            dfs(next, depth+1, eng+gansun)
            visited[next] -=1
            tree[node][next] = gansun
            tree[next][node] = gansun



T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    tree = [[0 for _ in range(V+1)] for _ in range(V+1)]
    for _ in range(E):
        a, b, w = map(int, input().split())
        tree[a][b] = w
        tree[b][a] = w
    min_eng = 10000
    for i in range(V):
        visited= [0 for _ in range(V+1)]
        visited[i] = 1
        dfs(i, 0, 0)
    print('#{} {}'.format(tc, min_eng))
