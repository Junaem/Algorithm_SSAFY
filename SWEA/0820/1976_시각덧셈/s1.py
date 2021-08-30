import sys

sys.stdin = open('input.txt')

def calc(h1, m1, h2, m2):
    h = ((h2 + h1 + (m1 + m2) // 60) - 1) % 12 + 1
    m = (m1 + m2) % 60
    return h, m



T = int(input())
for tc in range(1, T+1):
    h1, m1, h2, m2 = map(int, input().split())
    print('#{}'.format(tc), *calc(h1, m1, h2, m2))