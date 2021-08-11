import sys
import timeit
start_time = timeit.default_timer()
sys.stdin = open('input.txt')

def search(): # 하나의 tc를 실행하는 함수
    li = [ [] * 100 for _ in range(100)] # 필요한 100 * 100 크기의 배열
    # 0을 초기 max값으로 쓰려고 초기화한 게 아니고, li[0]의 합을 초기값으로 쓸려고 만들었다.
    my_max = 0
    # 입력을 받음과 동시에 my_max의 초기값이 될 li[0]의 합을 구한다.
    for i in range(100):
        li[i] = list(map(int, input().split()))
        my_max += li[0][i]
    # 'i' for문을 돌 때 대각선 값을 구할 것이다
    sum_dash, sum_rdash = 0, 0
    for i in range(100):
        # 'k' for문을 돌며 행, 열의 합을 구한다.
        sum_row, sum_col = 0, 0
        for k in range(100):
            sum_row += li[i][k]
            sum_col += li[k][i]
        # max 함수의 역할을 두 개의 if문으로 실시
        if sum_row < sum_col :
            sum_row = sum_col
        if my_max < sum_row :
            my_max = sum_row
        # 대각선 합 하나씩 더하기
        sum_dash += li[i][i]
        sum_rdash += li[i][99-i]
    # 역시 max를 찾는 if문
    if sum_dash < sum_rdash :
        sum_dash = sum_rdash
    if my_max < sum_dash:
        my_max = sum_dash

    return my_max

for tc in range(1, 10+1):
    input()
    print('#{} {}'.format(tc, search()))

terminate_time = timeit.default_timer()  # 종료 시간 체크

print("%f초 걸렸습니다." % (terminate_time - start_time))