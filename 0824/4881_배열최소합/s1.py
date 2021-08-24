import sys

sys.stdin = open('input.txt')

def sqr_min(cnt, sums):
    global min_sum # 글로벌 변수에 접근하기 위해 사용
    if cnt == N : # N까지 반복 후 그 값이 min보다 작으면
        if sums < min_sum:
            min_sum = sums  # min에 저장
        return
    elif sums > min_sum : # N보다 cnt가 작은데도 sums가 크면
        return # 건너뛰기

    for i in range(N):
        if not used[i]: # 아직 안 쓴 i를 골라
            used[i] = True # 사용 표시 후 더한 값으로 다시 재귀한다.
            sqr_min(cnt+1, sums + sqr[cnt][i]) # 카운트는 카운트임과 동시에 행의 인덱스다.
            used[i] = False # 사용 표시를 다시 지운다.

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    sqr = [list(map(int, input().split())) for _ in range(N)]
    used = [False] * N # 사용했는지 확인
    min_sum = 500 # 최소값을 저장하기 위한 수
    sqr_min(0, 0) # 재귀 실행
    print('#{} {}'.format(tc, min_sum))