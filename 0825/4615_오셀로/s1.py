import sys

sys.stdin = open('input.txt')

def oselo(board, n, m):
    for _ in range(m):
        x, y, clr = map(int, input().split())
        x, y = x-1, y-1
        board[y][x] = clr

        for i in range(0, x):
            if board[y][i] == clr:
                for k in range(i, x):
                    if board[y][k]:
                        board[y][k] = clr
        for i in range(x, n):
            if board[y][i] == clr:
                for k in range(x, i):
                    if board[y][k]:
                        board[y][k] = clr
        for i in range(0, y):
            if board[x][i] == clr:
                for k in range(i, y):
                    if board[x][k]:
                        board[x][k] = clr
        for i in range(y, n):
            if board[x][i] == clr:
                for k in range(y, i):
                    if board[x][k]:
                        board[x][k] = clr

        for i in range(n):
            if not (0 <= y-i < n and 0 <= x-i < n):
                if board[y-i][y-i]





    return board




T = int(input())
# for tc in range(1, T+1):
N, M = map(int, input().split())
board = [[0 for _ in range(N)] for _ in range(N)]
mid = N//2
board[mid-1][mid-1], board[mid-1][mid], board[mid][mid-1], board[mid][mid] = 2, 1, 1, 2

print(oselo(board, N, M))
