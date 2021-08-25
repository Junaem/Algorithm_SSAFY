import sys

sys.stdin = open('input.txt')


def subsc(N, a, b):
    max_s = a if a < b else b
    min_s = 0
    if a + b > N:
        min_s = a + b - N
    return max_s, min_s

T = int(input())
for tc in range(1, T+1):
    N, A, B = map(int, input().split())
    print('#{}'.format(tc), *subsc(N, A, B))