from collections import deque
import sys

sys.stdin = open('input.txt')

DLT = [(1, 0), (0, 1), (-1, 0), (0, -1)]

def check(mat):
    max_move = 0
    room_num = 0
    for i in range(N):
        for j in range(N):
            move = bfs(i, j)
            tmp_num = mat[i][j]
            if move > max_move:
                max_move = move
                room_num = tmp_num
            if move == max_move:
                room_num = tmp_num if tmp_num<room_num else room_num
    return room_num, max_move


def bfs(i, j):
    q = deque([(i, j)])
    move = 1
    while q:
        y, x = q.popleft()
        now = mat[y][x]
        for m in range(4):
            ny, nx = y + DLT[m][0], x + DLT[m][1]
            if ny in range(N) and nx in range(N):
                if mat[ny][nx] == now+1 :
                    move += 1
                    q.append((ny, nx))
                    break

    return move


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    print('#{}'.format(tc), *check(mat))