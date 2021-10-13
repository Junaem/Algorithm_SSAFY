import sys

sys.stdin = open('input.txt')

def dfs(prd, price, points):
    global min_price

    if price > min_price:
        return
    if prd==N-1:
        min_price = price



    for fc in points[prd]:
        idx = fc[0]
        if running[idx]:
            continue
        running[idx] = True
        dfs(prd+1, price+mat[prd][idx], points)
        running[idx] = False

def find_best(mat):
    points = [[0 for _ in range(N)] for _ in range(N)]
    fac_mat= [[0 for _ in range(N)] for _ in range(N)]
    for pr in range(N):
        line = sorted(enumerate(mat[pr]), key=lambda x: x[1])
        for i in range(N):
            idx = line[i][0]
            points[pr][idx] = i

            fac_mat[i][pr] = mat[pr][i] # 공장 위주로 배열 회전
    for fc in range(N):
        prds = sorted(enumerate(mat[pr]), key=lambda x: x[1])
        for i in range(N):
            idx = prds[i][0]
            points[idx][fc] = i

    for line_i in range(N):
        line = points[line_i]
        line = sorted(enumerate(line), key=lambda x: x[1])
        points[line_i] = line
    dfs(-1, 0, points)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    running = [False for _ in range(N)]
    able_fct = set(range(N))
    min_price = N*100
    find_best(mat)
    print('#{} {}'.format(tc, min_price))