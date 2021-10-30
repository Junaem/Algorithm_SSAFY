import sys
fro
sys.stdin = open('input.txt')

Dy = (1, 0, -1, 0)
Dx = (0, 1, 0, -1)

def boom(y, x, cnt, eng, drc, tmp_mat):
    global temp_li
    if cnt == eng: return
    if [y, x] not in temp_li:
        temp_li.append([y, x])

    for d in range(4):
        ny, nx = y + Dy[d], x + Dx[d]
        if ny in range(W) and nx in range(H) and tmp_mat[ny][nx]:
            boom(ny, nx, cnt+1, eng, d, tmp)



def check(tmp_mat):
    global b_li, temp_li
    max_idx, max_num =[0, 0], 0
    for i in range(W):
        for j in range(H-1, -1, -1):
            if tmp_mat[i][j]:
                temp_li = []
                boom(i, j, 0, tmp_mat[i][j], -1, tmp_mat)
                sim_num = len(temp_li)
                if sim_num > max_num:
                    max_idx, max_num = [i, j], sim_num
                    b_li = temp_li
                break

    for block in b_li:
        y, x = block[0], block[1]
        tmp_mat[y][x] = 0

    for i in range(W):
        for j in range(H-1, -1, -1):
            if not tmp_mat[i][j]:
                tmp_mat[i].pop(j)
        while len(tmp_mat[i]) < H:
            tmp_mat[i].append(0)



T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    org_mat = [list(map(int, input().split())) for _ in range(H)]
    mat = [[0 for _ in range(H)] for _ in range(W)]
    for i in range(H):
        for j in range(W):
            mat[j][-i-1]  = org_mat[i][j]
    b_li, temp_li = [], []
    print(mat)
    for _ in range(N): check(mat)

    answer = 0
    for i in range(W):
        for j in range(H):
            if mat[i][j]:
                answer +=1
    print(mat)
    print(answer)