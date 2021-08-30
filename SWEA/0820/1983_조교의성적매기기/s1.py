import sys
import timeit

sys.stdin = open('input.txt')

def merge_sort(li): # 병합정렬
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
    scores = [0] # 인덱스를 그대로 사용하기 위해 [0]에 0을 넣음
    for i in range(n):
        mid, fin, asg = map(int, input().split())
        scores += [mid*35 + fin*45 + asg*20] # 총합 점수 계산
    sorted_score = merge_sort(scores)[::-1] # 오름차순 정렬을 위해 list 거꾸로 사용

    grades = ['', 'A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-'] # 인덱스 편의를 위해 ''를 넣음
    for per in range(1, 10):
        if scores[k] > sorted_score[per * n // 10]: # 각 학점 경계의 점수를 k의 점수와 비교
            return grades[per] # k의 점수가 더 높으면 리턴
    return 'D0' # 해당 없으면 D0




T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    print('#{} {}'.format(tc, grade(N, K)))




