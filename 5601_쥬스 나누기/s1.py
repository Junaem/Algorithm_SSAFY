import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    st = ('1/' + str(N) + ' ') * N
    print('#{} {}'.format(tc, st))