import sys

sys.stdin = open('input.txt')

def is_pal_n(n): # 수를 문자열로 바꾼 뒤 회문 확인
    num = str(n)
    for i in range(len(num) // 2):
        if num[i] != num[-i - 1]:
            return False
    return True


def check_nums(a, b):
    cnt = 0
    for num in range(a, b + 1):
        root = num ** 0.5 # 제곱근(float형태)
        if root.is_integer() and is_pal_n(int(root)) and is_pal_n(num): # root가 정수이고, 회문이며, num도 회문이면
            cnt += 1 # 카운트 +1
    return cnt


T = int(input())
for tc in range(1, T + 1):
    A, B = map(int, input().split())
    print('#{} {}'.format(tc, check_nums(A, B)))