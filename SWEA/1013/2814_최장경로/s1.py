import sys
sys.stdin = open('input.txt')


def farthest(node, depth):
    est = depth

    for next in range(1, N+1):
        if tree[node][next]:
            if next in visited: continue
            visited.add(next)
            rst = farthest(next, depth+1)
            if rst > est:
                est = rst
            visited.remove(next)

    return est


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    tree = [[False for _ in range(N+1)] for _ in range(N+1)]

    for _ in range(M):
        a, b = map(int, input().split())
        tree[a][b] = True
        tree[b][a] = True

    answer = 0
    for i in range(1, N+1):
        visited = set({i})
        answer = max(answer, farthest(i, 1))
    print('#{} {}'.format(tc, answer))