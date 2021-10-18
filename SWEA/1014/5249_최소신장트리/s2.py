from collections import deque
import sys

sys.stdin = open('input.txt')

def route(gansuns):
    gansuns = deque(gansuns)
    MST = []

    while len(MST) < V and gansuns:
        gansun = gansuns.popleft()
        a, b, w = gansun
        if find_set(a) == find_set(b): continue
        union(a, b)
        MST.append(w)
    return sum(MST)


def find_set(x):
    if x == P[x] : return x
    return find_set(P[x])

def union(x, y):
    P[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    gansuns = []
    for _ in range(E):
        gansuns.append(list(map(int, input().split())))
    gansuns.sort(key= lambda x: x[2])
    P = [i for i in range(V+1)]
    print('#{} {}'.format(tc, route(gansuns)))