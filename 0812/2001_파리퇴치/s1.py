import sys

sys.stdin = open('input.txt')

def flies(n, m):
    li = [list(map(int, input().split())) for _ in range(n)]
    sum_max = 0 # 한번의 잡을 수 있는 파리수 중 max
    for i in range(n - m + 1): #파리채 x축 조준
        for i2 in range(n - m +1): # y축 조준
            f_sum = 0
            for k in range(m): # x축 너비
                for k2 in range(m): # y축 너비
                    f_sum += li[i+k][i2+k2] # 철썩
            if sum_max < f_sum :
                sum_max = f_sum # max값 저장
    return sum_max

T = int(input())

for tc in range(1, 1 + T):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, flies(N, M)))