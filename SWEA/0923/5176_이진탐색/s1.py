import sys

sys.stdin = open('input.txt')

def route(n):
    rtn = 0
    while n>0:
        rtn += 1
        n //= 2
    return rtn

def treemaking(n):  # 4 2 6 1 3 5
    tree = [0]
    rt = route(n-1) # route(n-1)
    size = 2 ** rt

    queue = [ n // 2 +1 ] # ()n - (size//2)

    while queue:
        num = queue.pop(0)
        tree.append(num)

        if len(tree) == n +1:
            break
        pl_mi = 2 ** (rt - route(len(tree)+1))
        queue.append(num - pl_mi)
        queue.append(num + pl_mi)
    return tree, tree[1], tree[n//2]

def treemaking2(n):
    for num in range(1, n+1):
        num


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{}'.format(tc), *treemaking(N))




    # mid = route(N) // 2
    # def insert(n, m):
    #     head = 0
    #     if n > m:
    #         head = 1
    #     if tree[m][head]:
    #         insert(n, tree[m][head])
    #     else:

    # has_parent = [[False] for - in range(N + 1)]


    # def insult(n):
    #     for i in range(1, n):
    #
    #
    # for n in range(1, N + 1):
    #     insert(n, mid)