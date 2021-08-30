import sys

sys.stdin = open('input.txt')


def spc_sort(n, li):
    ret_li =[]
    for i in range(n//2):
        max_i = -1
        min_i = -1
        for j in range(i*2 , n):
            if li[j] > li[max_i] :
                max_i = j
                li[i * 2], li[j] = li[j], li[i*2]
            if li[j] < li[min_i] :
                min_i = j
                li[i * 2 + 1], li[j] = li[j], li[i*2 + 1]

    # 10개만 출력하기 위해 slice 후 return
    return li[:10]


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    # 순창님의 너무나 아름다운 list출력법을 배워왔다.
    print('#{}'.format(tc), *spc_sort(n, li))
