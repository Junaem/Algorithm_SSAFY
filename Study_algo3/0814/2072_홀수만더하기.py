import sys

sys.stdin = open('2072.txt')

def odd_sum(li):
    rtn = 0
    for i in li:
        if i % 2:
            rtn += i
    return rtn


T = int(input())

for tc in range(1, T+1):
    li = list(map(int, input().split()))
    print('#{} {}'.format(tc, odd_sum(li)))