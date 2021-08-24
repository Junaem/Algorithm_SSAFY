import sys

sys.stdin = open('input.txt')

def is_pal_n(n): # 숫자를 문자열로 바꾼 뒤 회문인지 확인
    num = str(n)
    for i in range(len(num)//2):
        if num[i] != num[-i-1]:
            return False
    return True

def check_nums(A, B):
    a, b = A ** 0.5, B ** 0.5  # map(lambda x: x ** 0.5, [A, B])
    if a - int(a):      # a가 정수가 아닌 경우 +1, if a.is_integer()도 사용 가능
        a += 1
    a, b = map(int, (a, b)) # A, B의 제곱근인 a, b를 사용
    cnt = 0
    for num in range(a, b+1): # 두 제곱근 사이의 정수를 제곱한 뒤
        if is_pal_n(num) and is_pal_n(num ** 2): # 회문 확인
            cnt += 1
    return cnt



T = int(input())
for tc in range(1, T+1):
    A, B = map(int, input().split())
    print('#{} {}'.format(tc, check_nums(A, B)))