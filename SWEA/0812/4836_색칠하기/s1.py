import sys

sys.stdin = open('input.txt')
# 하나의 테스트 케이스를 수행하는 함수
def coloring(n):
    li = [[0] * 10 for _ in range(10)] # 10 * 10의 빈 배열
    cnt = 0 # 색이 중첩된 부분의 갯수 cnt
    # n번 색칠하는 for문.
    for _ in range(n):
        col_li = list(map(int, input().split()))
        for i in range(col_li[1], col_li[3] +1): # 가로 범위
            for k in range(col_li[0], col_li[2] + 1): # 세로 범위
                # 칠하려는 칸이 현재 색과 다른 하나의 색만 칠해져 있으면
                if li[i][k] > 0 and li[i][k] != col_li[4]:
                    li[i][k] = -1 # -1(중첩을 나타내는 숫자)로 바꾸고
                    cnt += 1 # 중첩된 칸 수를 늘린다.
                else : # 아니면 현재 색으로 칠
                    li[i][k] = col_li[4]
    return cnt

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    print('#{} {}'.format(tc, coloring(N)))