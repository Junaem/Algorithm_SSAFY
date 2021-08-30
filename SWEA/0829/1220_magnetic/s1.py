import sys

sys.stdin = open('input.txt')

def magnito(matrix, N):
    cnt = 0
    for r in range(N):
        for c in range(N):
            if matrix[r][c] == 1:
                for dr in range(r, N):
                    if matrix[dr][c] == 1:
                        matrix[dr][c] = 0
                    elif matrix[dr][c] == 2:
                        cnt +=1
                        break
    return cnt





for tc in range(1, 11):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, magnito(matrix,N)))