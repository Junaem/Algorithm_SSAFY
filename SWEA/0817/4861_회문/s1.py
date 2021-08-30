import sys

sys.stdin = open('input.txt')

# 회문인지 확인하는 함수
def is_aba(st):
    for i in range(len(st) // 2):
        if st[i] != st[- i - 1]:
            return False
    return True

def abcdcba(n, m):
    li = [input() for _ in range(n)]
    for i in range(n): # 검사할 행,열의 인덱스
        for j in range(n - m + 1): # 회문의 시작 단어 위치
            st_r = '' # 가로로 찾을 string
            st_c = '' # 세로로 찾을 string
            for k in range(m): # m의 길이만큼 str을 쌓는다.
                st_r += li[i][j+k]
                st_c += li[j+k][i]
            # 찾은 글자가 회문이면 return
            if is_aba(st_r):
                return st_r
            elif is_aba(st_c):
                return st_c


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, abcdcba(N, M)))