import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(T):
    # N과 M, 리스트를 받아온다.
    N, M = map(int, input().split())
    li = list(map(int, input().split()))
    # min을 최대값, max를 최소값으로 초기화
    n_min = 500000
    n_max = 0

    #부분의 시작부분을 i로 정의
    for i in range(N-M+1):
        n_sum = 0 #부분합을 저장할 값
        # 부분의 범위를 돌며 부분합을 구한다. 석준님의 코드를 보고 slice를 활용했다.
        for k in li[i: i+M]:
            n_sum += k

        # 구한 부분합이 최대값, 최소값이라면 저장
        if n_sum > n_max :
            n_max = n_sum
        if n_sum < n_min :
            n_min = n_sum
<<<<<<< HEAD
    # 최대값과 최소값의 차이를 형식에 맞게 출력
=======

>>>>>>> 7f5602502e6c05090b6e3ac648edc4a7999a1906
    print('#{} {}'.format(t+1, n_max - n_min))

