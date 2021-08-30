import sys
import timeit
# 실행 속도에 중점을 두고 만들었다.
# start_time = timeit.default_timer()
sys.stdin = open('sort_input.txt')


def merge_sort(li):
    half = len(li)//2
    if half:
        lft = merge_sort(li[:half])
        rgt = merge_sort(li[half:])
        li=[]
        while lft and rgt:
            if lft[0] < rgt[0]:
                li.append(lft.pop(0))
            else :
                li.append(rgt.pop(0))
        if lft:
            li += lft
        else :
            li += rgt
    return li

def merge_sort2(li):
    half = len(li)//2
    if half:
        lft = merge_sort2(li[:half])[::-1]
        rgt = merge_sort2(li[half:])[::-1]
        li=[]
        while lft and rgt:
            if lft[-1] < rgt[-1]:
                li.append(lft.pop())
            else :
                li.append(rgt.pop())
        if lft:
            li += lft[::-1]
        else :
            li += rgt[::-1]
    return li

def bubble_sort(boxes_height):
    for i in range(len(boxes_height)-1, 0, -1):
        for j in range(0, i):
            if boxes_height[j] > boxes_height[j+1] :
                boxes_height[j], boxes_height[j+1] = boxes_height[j+1], boxes_height[j]
    return boxes_height






def flatten(dump_n, dumps):

    start_time = timeit.default_timer()
    srt = sorted(dumps)
    terminate_time = timeit.default_timer()
    print("sorted는 %f초 걸렸습니다." % (terminate_time - start_time))

    start_time = timeit.default_timer()
    bub = bubble_sort(dumps)
    terminate_time = timeit.default_timer()
    print("bub는 %f초 걸렸습니다." % (terminate_time - start_time))

    start_time = timeit.default_timer()
    mrg = merge_sort(dumps)
    terminate_time = timeit.default_timer()
    print("mrg는 %f초 걸렸습니다." % (terminate_time - start_time))

    start_time = timeit.default_timer()
    mrg2 = merge_sort2(dumps)
    terminate_time = timeit.default_timer()
    print("mrg2는 %f초 걸렸습니다." % (terminate_time - start_time))
    print(srt == mrg, srt == mrg2)
    print()

for tc in range(1, 11):
    Dump_n = int(input())
    Dumps = list(map(int, input().split()))
    print(tc)
    flatten(Dump_n, Dumps)

# terminate_time = timeit.default_timer()  # 종료 시간 체크

# print("%f초 걸렸습니다." % (terminate_time - start_time))