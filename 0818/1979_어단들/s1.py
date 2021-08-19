import sys

sys.stdin = open('input.txt')

def cross(n, key):
    li = [list(map(int, input().split())) for _ in range(n)]
    cnt = 0 # key가 들어갈 수 있는 빈 칸의 갯수
    for i in range(n):
        for k in range(n):
            # 행으로 넣을 수 있는 것들 확인
            # 현재 칸이 빈 칸의 시작점이 맞는지 확인
            if li[i][k] == 1 and (k == 0 or li[i][k - 1] == 0) :
                k_end = k # 빈 칸의 길이를 확인
                while k_end + 1 < n and li[i][k_end + 1]:
                    k_end += 1
                if k_end - k == key - 1: # 빈 칸의 길이가 key와 같으면 cnt에 +1
                    cnt += 1
            # 열로 넣을 수 있는 것도 같은 방식으로 확인
            if li[k][i] and (k == 0 or not li[k - 1][i]):
                k_end = k
                while k_end + 1 < n and li[k_end + 1][i]:
                    k_end += 1
                if k_end - k == key - 1:
                    cnt += 1
    return cnt


T = int(input())

for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    print('#{} {}'.format(tc, cross(N, K)))