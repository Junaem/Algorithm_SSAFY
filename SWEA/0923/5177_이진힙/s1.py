import sys

sys.stdin = open('input.txt')

def treemaking(N, li):
    def compare(idx):
        if idx // 2 :
            prn = idx // 2
            if tree[prn] > tree[idx]:
                tree[idx], tree[prn] = tree[prn], tree[idx]
                compare(prn)

    for num in li:
        for idx in range(1, N+1):
            if not tree[idx]:
                tree[idx] = num
                compare(idx)
                break

    rtn = 0
    while N:
        N //= 2
        rtn += tree[N]
    return rtn




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    tree = [0 for _ in range(N+1)]
    print('#{} {}'.format(tc, treemaking(N, li)))