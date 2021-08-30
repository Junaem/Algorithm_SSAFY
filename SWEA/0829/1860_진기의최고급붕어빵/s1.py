import sys

sys.stdin = open('input.txt')


def boong(n, m, k):
    customers = sorted(list(map(int, input().split())))
    stock = 0
    sec = 0
    if not customers[0]:
        return 'Impossible'
    while customers:
        sec += 1
        if sec % m == 0:
            stock += k
        while customers and customers[0] <= sec:
            customers.pop(0)
            stock -=1
        if stock < 0 :
            return 'Impossible'
    return 'Possible'





T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    print('#{} {}'.format(tc, boong(N, M, K)))