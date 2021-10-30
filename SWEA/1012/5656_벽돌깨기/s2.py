import sys
from collections import deque
import copy


sys.stdin = open('input.txt')

Dy = (1, 0, -1, 0)
Dx = (0, 1, 0, -1)

def boom(i, j, tmp_mat):
    ttmp_mat = copy.deepcopy(tmp_mat)
    q = deque()
    q.append((i, j))
    b_cnt = 0
    while q:
        y, x = q.popleft()
        num = ttmp_mat[y][x]
        if not num: continue
        ttmp_mat[y][x] = 0
        b_cnt += 1

        for d in range(4):
            for n in range(1, num):
                ny, nx = y + Dy[d]*n, x + Dx[d]*n
                if ny in range(W) and nx in range(len(ttmp_mat[ny])) and ttmp_mat[ny][nx]:
                    q.append((ny, nx))

    return ttmp_mat, b_cnt

def check(mat, depth, cnt):
    global max_cnt


    if cnt > max_cnt:
        max_cnt = cnt
    if depth == N : return

    for i in range(W):
        tmp_mat = copy.deepcopy(mat)
        if tmp_mat[i]:
            j = len(tmp_mat[i])-1
            if tmp_mat[i][j]:
                ttmp_mat, t_cnt = boom(i, j, tmp_mat)

                for w in range(W):                      # 0 없애고 0 넣기
                    for h in range(len(ttmp_mat[w])-1, -1, -1):
                        if not ttmp_mat[w][h]:
                            ttmp_mat[w].pop(h)

                check(ttmp_mat, depth+1, cnt + t_cnt)


T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    org_mat = [list(map(int, input().split())) for _ in range(H)]
    mat = [[0 for _ in range(H)] for _ in range(W)]
    for i in range(H):
        for j in range(W):
            mat[j][-i-1]  = org_mat[i][j]

    blocks = 0
    for i in range(W):
        for j in range(H):
            if mat[i][j]:
                blocks += 1

    for i in range(W):  # 0 없애고 0 넣기
        for j in range(len(mat[i])-1, -1, -1):
            if not mat[i][j]:
                mat[i].pop(j)
            else:
                break
    max_cnt = 0
    check(mat, 0, 0)
    print('#{} {}'.format(tc, blocks - max_cnt))