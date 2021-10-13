import sys
from collections import deque
sys.stdin = open('input.txt')

def merge_sort(li):
    global rst
    half = len(li)//2
    if not half:
        return li

    a = deque(merge_sort(li[:half]))
    b = deque(merge_sort(li[half:]))
    if a[-1] > b[-1]:
        rst += 1

    rtn = []
    while a and b:
        if a[0] < b[0]:
            rtn.append(a.popleft())
        else:
            rtn.append(b.popleft())
    if a:
        rtn += a
    else:
        rtn += b

    return rtn



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    rst = 0
    li = merge_sort(li)
    print('#{} {} {}'.format(tc, li[N//2], rst))