import sys

sys.stdin = open('input.txt')

def is_99dan(n):
    for i in range(1, 10):
        a = n/i
        if not n%i and a in range(1, 10) :
            return 'Yes'
    return 'No'




T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, is_99dan(N)))