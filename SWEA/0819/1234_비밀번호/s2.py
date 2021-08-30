import sys

sys.stdin = open('input.txt')

def password(n, nums):
    pw = ''
    for i in nums:
        if pw and pw[-1] == i:
            pw = pw[:-1]
        else :
            pw += i
    return pw


for tc in range(1, 11):
    N, nums = input().split()
    print('#{} {}'.format(tc, password(int(N), nums)))