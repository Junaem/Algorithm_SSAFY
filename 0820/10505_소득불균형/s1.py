import sys

sys.stdin = open('input.txt')

def income(n):
    li = list(map(int, input().split()))

    li_avg = 0
    for i in li:
        li_avg += i
    li_avg /= n

    cnt = 0
    for i in li:
        if i <= li_avg:
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, income(N)))
