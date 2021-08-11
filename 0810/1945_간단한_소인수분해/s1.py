import sys

sys.stdin = open('input.txt')

# n값과 소수를 받아 나눌 수 없을 때까지 나누는 함수.
def soinsu_func(n, soin):
    times = 0
    while not n % soin:
        n /= soin
        times += 1
    # 나누어진 n과 나눈 횟수를 리턴한다.
    return n, times



T = int(input())

for t in range(T):
    N_original = int(input())
    N = N_original
    N, a = soinsu_func(N, 2)
    N, b = soinsu_func(N, 3)
    N, c = soinsu_func(N, 5)
    N, d = soinsu_func(N, 7)
    N, e = soinsu_func(N, 11)

    print('#{} {} {} {} {} {}'.format(t+1, a, b, c, d, e))
