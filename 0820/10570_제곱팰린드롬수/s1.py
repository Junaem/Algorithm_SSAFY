import sys

sys.stdin = open('input.txt')

def is_pal_n(n):
    num = str(n)
    for i in range(len(num) // 2):
        if num[i] != num[-i - 1]:
            return False
    return True


def check_nums(a, b):
    cnt = 0
    for num in range(a, b + 1):
        root = num ** 0.5
        if root.is_integer() and is_pal_n(int(root)) and is_pal_n(num):
            cnt += 1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    print('#{} {}'.format(tc, check_nums(A, B)))