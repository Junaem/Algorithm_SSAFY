import sys

sys.stdin = open('input.txt')

def bin_search(li, l, r, t, side):

    if l==N or r==0: return 0

    m = (l+r)//2
    if A[m] == t:
        return 1
    if l>=r : return 0


    rtn = 0
    if t < A[m] and side!='l':
        rtn = bin_search(A, l, m-1, t, 'l')
    elif t > A[m] and side!='r':
        rtn = bin_search(A, m+1, r, t, 'r')

    return rtn


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))     # 진짜 너무하네 이 사람들
    B = list(map(int, input().split()))
    rst = 0
    for n in B:
        rst += bin_search(A, 0, N-1, n, 0)
    print('#{} {}'.format(tc, rst))