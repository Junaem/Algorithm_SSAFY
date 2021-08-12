import sys

sys.stdin = open('input.txt')


def recur(num, n_sum, cnt):
    if cnt == N: # N개 만큼 숫자를 사용했다면 부분합이 K인지 검사
        if n_sum == K: # 같으면 1
            return 1
        else : # 다르면 0
            return 0
    # num을 포함하고 가능한 부분합의 갯수를 rec_sum에 저장할 것이다.
    rec_sum = 0
    for i in range(num+1, 13): # num보다 큰 수를 돌며 다시 재귀, 그 값을 더하여 리턴
        rec_sum += recur(i, n_sum + i, cnt + 1)
    return rec_sum


T = int(input())

for tc in range(1, T+1):
    li = list(range(1, 13))
    N, K = map(int, input().split())
    print('#{} {}'.format(tc, recur(0, 0, 0)))