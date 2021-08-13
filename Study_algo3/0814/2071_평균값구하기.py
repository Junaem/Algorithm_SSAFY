import sys

sys.stdin = open('2071.txt')

def my_avg(li):
    rtn = 0
    for i in li:
        rtn += i
    rtn = rtn / len(li)
    if rtn - int(rtn) >= 0.5:
        rtn += 1
    return int(rtn)


T = int(input())

for tc in range(1, T+1):
    li = list(map(int, input().split()))
    print('#{} {}'.format(tc, my_avg(li)))