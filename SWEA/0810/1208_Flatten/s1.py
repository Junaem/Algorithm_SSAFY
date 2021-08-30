import sys
import timeit
# 실행 속도에 중점을 두고 만들었다.
start_time = timeit.default_timer()
sys.stdin = open('input.txt')

# 테스트 케이스 하나를 처리할 함수
def flatten(dump_n, dumps):
    # 각 높이 별로 갯수를 리스트에 담았다.
    height = [0] * 101
    for dump in dumps:
        height[dump] += 1
    # 시작은 높은거 100, 낮은거 1에서 시작
    highest = 100
    lowest = 1
    # 한번의 평탄화 작업을 하는 내부 함수
    def move():
        # 내부에서 인접 함수의 인자에 접근하기 위한 nonlocal
        nonlocal highest
        # highest 높이인 칸이 0이면 0이 아닐 때 까지 내려간다.
        while not height[highest]:
            highest -= 1
        # highest 높이의 숫자를 -1, 한칸 낮은 숫자를 +1
        height[highest] -= 1
        height[highest - 1] += 1
        # lowest는 highest의 반대로 같은 작업을 해준다.
        nonlocal lowest
        while not height[lowest]:
            lowest += 1
        height[lowest] -= 1
        height[lowest + 1] += 1

    # 주어진 dump횟수만큼 move 함수를 실행
    for i in range(dump_n):
        move()
    # 리턴하기 전에 현재 highest나 lowest의 값이 비어있는지 확인
    while not height[highest]:
        highest -= 1
    while not height[lowest]:
        lowest += 1
    # highest와 lowest의 차를 반환한다.
    return highest - lowest


for tc in range(1, 11):
    Dump_n = int(input())
    Dumps = list(map(int, input().split()))

    print('#{} {}'.format(tc, flatten(Dump_n, Dumps)))

terminate_time = timeit.default_timer()  # 종료 시간 체크
#
print("%f초 걸렸습니다." % (terminate_time - start_time))