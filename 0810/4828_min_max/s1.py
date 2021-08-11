import sys

sys.stdin = open("input.txt")

T = int(input())

for i in range(T):
    N = int(input())
    # my_max와 my_min값을 나올 수 있는 최소, 최대값으로 초기화
    my_max = 1
    my_min = 1000000
    li = list(map(int, input().split()))

    # 리스트를 돌며 최대값, 최소값 저장장
   for k in li:
        if k > my_max:
            my_max = k
        if k < my_min:
            my_min = k
    print('#{} {}'.format(i+1, my_max - my_min))