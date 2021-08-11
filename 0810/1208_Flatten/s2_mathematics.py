import sys
import timeit

# 실행 속도에 중점을 두고 만들었다.
start_time = timeit.default_timer()
sys.stdin = open('input.txt')


def flatten(dump_n, dumps):
    # 각 높이 별로 갯수를 리스트에 담았다.
    height = [0] * 101
    for dump in dumps:
        height[dump] += 1

    highest = 100
    lowest = 1

    while not height[highest]:
        highest -= 1
    while not height[lowest]:
        lowest += 1

    h_sum = 0
    h_last = 0
    for i in range(highest, 0, -1):
        if h_sum * (highest - i) > dump_n:
            h_last = i
            break
        h_sum += height[i]

    l_sum = 0
    l_last = 0
    for i in range(lowest, 101):
        if l_sum * (i - lowest) > dump_n:
            l_last = i
            break
        l_sum += height[i]

    print(h_last - l_last)
    h_crawl = [highest, height[highest]]
    while h_crawl[1] < h_sum :
        h_crawl[1] = (h_crawl[1] * 2 + height[h_crawl[0] - 1])
        h_crawl[0] -= 1

    l_crawl = [lowest, height[lowest]]
    while l_crawl[1] < l_sum:
        l_crawl[1] = (l_crawl[1] * 2 + height[l_crawl[0] - 1])
        l_crawl[0] += 1
    print(h_crawl[0] - l_crawl[0])




for tc in range(1, 11):
    Dump_n = int(input())
    Dumps = list(map(int, input().split()))

    print('#{} {}'.format(tc, flatten(Dump_n, Dumps)))

terminate_time = timeit.default_timer()  # 종료 시간 체크
#
print("%f초 걸렸습니다." % (terminate_time - start_time))