import sys

sys.stdin = open('input.txt')

def bub_sort(n, li): # 버블 소트 구현
    for _ in range(n):
        for i in range(n-1):
            if li[i] > li[i+1]:
                li[i], li[i+1] = li[i+1], li[i]
    return li


def spc_sort(n, li):
    li = bub_sort(n, li) # 버블 소트 실행
    ret_li = [0] * n # 리턴할 리스트를 출력하기 좋게 str형으로 만들었다.
    for i in range(n//2): # n값의 절반만큼 돌면서 조건에 맞게 ret_li에 할당
        ret_li[i * 2] = li[-(i+1)]
        ret_li[i * 2 + 1] = li[i]
    # 10개만 출력하기 위해 slice 후 return
    return ret_li[:10]



T = int(input())

for tc in range(1, T+1):
    n = int(input())
    li = list(map(int, input().split()))
    # 순창님의 너무나 아름다운 list출력법을 배워왔다.
    print('#{}'.format(tc), *spc_sort(n, li))