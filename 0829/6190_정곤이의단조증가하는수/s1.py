import sys

sys.stdin = open('input.txt')

def check(num):
    st_n = str(num)
    for i in range(1, len(st_n)):
        if st_n[i] < st_n[i-1]:
            return False
    return True


def makeX(N, li):
    rtn = 0
    for i in range(N-1):
        for j in range(i+1, N):
            x = li[i] * li[j]
            if check(x):
                if x > rtn:
                    rtn = x
    if rtn:
        return rtn
    else:
        return -1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    nums = list(map(int, input().split()))
    print('#{} {}'.format(tc, makeX(N, nums)))
