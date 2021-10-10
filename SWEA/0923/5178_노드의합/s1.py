import sys

sys.stdin = open('input.txt')

def search(node):
    if node > N:
        return 0
    if tree[node]:
        return tree[node]
    rtn = 0
    for i in range(2):
        rtn += search(2*node + i)
    return rtn


<<<<<<< HEAD
=======


>>>>>>> 80b45840e22dc7ff75df0b380c13db71775a85df
T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    tree = [0 for _ in range(N+1)]
    for _ in range(M):
        idx, val = map(int, input().split())
        tree[idx] = val
    print('#{} {}'.format(tc, search(L)))