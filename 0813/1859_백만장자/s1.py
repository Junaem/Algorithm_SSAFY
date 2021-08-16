import sys
import timeit
start_time = timeit.default_timer()

sys.stdin = open('input.txt')


def max_day(li): # list의 max값의 인덱스를 뒤에서부터 찾아주는 함수
    ret = 0
    for i in range(len(li)-1, -1, -1):
        if li[i] > li[ret] :
            ret = i
    return ret


def buza(n, prices): # 하나의 테스트 케이스를 수행하는 함수
    buy_day, sell_day = 0, max_day(prices) # 처음 사는 날은 0, 처음 파는 날은 가격이 가장 높은 날
    earns = 0

    while buy_day < n-1:
        profit = prices[sell_day] * (sell_day - buy_day)
        for day in range(buy_day, sell_day):
            profit -= prices[day]
        earns += profit
        buy_day = sell_day + 1

        tmp = max_day(prices[buy_day:]) + 1
        if tmp:
            sell_day += tmp
        else:
            buy_day += 1
            continue
    return earns

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))
    print('#{} {}'.format(tc, buza(N, prices)))

terminate_time = timeit.default_timer()
print("%f초 걸렸습니다." % (terminate_time - start_time))
