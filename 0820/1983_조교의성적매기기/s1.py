import sys
import timeit

sys.stdin = open('input.txt')

def merge_sort(li):
    half = len(li)//2
    if half:
        lft = merge_sort(li[:half])
        rgt = merge_sort(li[half:])
        li = []
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


def grade(n, k):
    scores = [0]
    for i in range(n):
        mid, fin, asg = map(int, input().split())
        scores += [mid*35 + fin*45 + asg*20]
    sorted_score = merge_sort(scores)[::-1]

    grades = ['', 'A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-']
    for per in range(1, 10):
        if scores[k] > sorted_score[per * n // 10]:
            return grades[per]
    return 'D0'




T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    print('#{} {}'.format(tc, grade(N, K)))




