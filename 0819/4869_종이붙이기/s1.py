import sys

sys.stdin = open('input.txt')

papers = [0 for _ in range(31)] # 메모이제이션
papers[1] = 1

def paper(n):
    if not papers[n]:
        if n % 2: # 홀수일 때는 전부 세로로 붙이는 경우는 경우의 수를 1밖에 증가 못 시켜서 - 1
            papers[n] = paper(n-1) * 2 - 1
        else : # 짝수일 때는 전부 세로 :-1, 전부 2x2: +1, 전부 가로: + 1의 경우의 수가 생겨서 총합 (-1+2) == +1
            papers[n] = paper(n-1) * 2 + 1
    return papers[n]


T = int(input())

for tc in range(1, T+1):
    N = int(input()) // 10
    print('#{} {}'.format(tc, paper(N)))