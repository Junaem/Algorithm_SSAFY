import sys

sys.stdin = open('input.txt')

def quick_sort(li, l, r):
    if l < r:
        li, s = partition(l, r)
        quick_sort(li, l, s-1)
        quick_sort(li, s+1, r)
    return li

def partition(l, r):
    pivot = li[l]

    i, j = l, r

    while i <= j:
        while i <= j and li[i] <= pivot:
            i+=1
        while i <= j and li[j] >= pivot:
            j-=1
        if i < j:
            li[i], li[j] = li[j], li[i]

    li[l], li[j] = li[j], li[l]

    return li, j



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    li = list(map(int, input().split()))
    li = quick_sort(li, 0, N-1)
    print('#{} {}'.format(tc, li[N//2]))