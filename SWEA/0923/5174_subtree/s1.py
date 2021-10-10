import sys

sys.stdin = open('input.txt')

def search(node):
    sum = 1
    for n in tree[node]:
        sum += search(n)
    return sum

T = int(input())
for tc in range(1, T+1):
    E, N = map(int, input().split())
    tree = [[] for _ in range(E+2)]
    li = list(map(int, input().split()))
    for i in range(E):
        a, b = li[2*i], li[2*i + 1]
        tree[a].append(b)
    print('#{} {}'.format(tc, search(N)))