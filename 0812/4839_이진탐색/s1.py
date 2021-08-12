import sys

sys.stdin = open('input.txt')

# 이진 검색, l, r은 양 쪽 끝, n은 찾아야할 숫자
def bin_search(l, r, n):
    now = (l + r) // 2
    if now == n : # 찾았으면 1을 리턴
        return 1
    elif now < n : # 현재값이 더 작으면 오른쪽 탐색
        return bin_search(now, r, n) + 1
    else : # 현재값이 더 크면 왼쪽 탐색
        return bin_search(l, now, n) + 1


# 횟수가 적은 쪽의 이름을 리턴
def fight(A, B):
    if A < B :
        return 'A'
    elif A > B :
        return 'B'
    else :
        return 0


T = int(input())

for tc in range(1, T + 1):
    P, aN, bN = map(int, input().split())
    A = bin_search(1, P, aN)
    B = bin_search(1, P, bN)
    print('#{} {}'.format(tc, fight(A, B)))