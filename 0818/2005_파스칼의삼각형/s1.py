import sys

sys.stdin = open('input.txt')
# 메모이제이션을 위한 파스칼 리스트
pascals = [[] for _ in range(11)]
pascals[1].append([1])

def pascal(n): # 재귀를 통해 풀었다.
    if not pascals[n]: # 파스칼[n]이 비어있을 경우 다음과 같이 채운다.
        pascals[n] = pascal(n-1) # 일단 n이전 층을 불러온다.     [1,2,1]
        new_li = [0] * n # 이번에 새로 만들 층                   [1,3,3,1]
        last_li = pascals[n][-1] # n-1에서 만든 층
        for i in range(n-1): # n-1의 각 값을 같은 인덱스, 같은 인덱스+1에 더해준다.
            new_li[i] += last_li[i]
            new_li[i+1] += last_li[i]
        pascals[n].append(new_li) # 그렇게 만든 층을 쌓는다.

    return pascals[n]

def print_pascal(li):
    for i in li:
        print(*i)
T = int(input())

for tc in range(1, 1+T):
    n = int(input())
    print('#{}'.format(tc))
    print_pascal(pascal(10))