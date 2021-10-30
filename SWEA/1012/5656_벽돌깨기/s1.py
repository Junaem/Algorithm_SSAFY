import sys
from collections import deque
import copy                     # 깊은 복사를 안 해서 계속 답이 안 나왔다.


sys.stdin = open('input.txt')

Dy = (1, 0, -1, 0)
Dx = (0, 1, 0, -1)

def boom(i, j, tmp_mat):
    ttmp_mat = copy.deepcopy(tmp_mat)
    q = deque()
    q.append((i, j))        # 시작점을 담은 큐
    b_cnt = 0               # 터뜨린 블록 갯수
    while q:
        y, x = q.popleft()
        num = ttmp_mat[y][x]
        if not num: continue    # 이미 0으로 바꿔놨다면 무시
        ttmp_mat[y][x] = 0      # 0으로 바꾸고 터뜨림 카운트 +1
        b_cnt += 1

        for d in range(4):      # 모든 방향으로
            for n in range(1, num):     # 폭발 범위 내의 블럭
                ny, nx = y + Dy[d]*n, x + Dx[d]*n       # 터뜨릴 블럭 좌표
                if ny in range(W) and nx in range(H) and ttmp_mat[ny][nx]: # 좌표가 유효하고 숫자가 0이 아니면
                    q.append((ny, nx))                                     # 큐에 넣어서 터뜨림

    return ttmp_mat, b_cnt      # 터뜨려진 매트릭스와 터진 횟수를 리턴

def check(mat, depth, cnt):
    global max_cnt


    if cnt > max_cnt:       # 맥스값보다 많이 터뜨리면 갱신
        max_cnt = cnt
    if depth == N : return  # N번 실행

    for i in range(W):              # 각 줄을 돌며 뭘 터뜨릴지 결정
        tmp_mat = copy.deepcopy(mat)        # 매트릭스 이전 매트릭스로 초기화
        for j in range(H-1, -1, -1):        # 제일 뒤에 하나를 골라 실행후 break
            if tmp_mat[i][j]:               # 값이 0이 아니면 터뜨림
                ttmp_mat, t_cnt = boom(i, j, tmp_mat)   # 터뜨린 결과 매트릭스와 t_cnt값을 저장

                for w in range(W):                      # 0 없애고 0 넣기
                    for h in range(H - 1, -1, -1):
                        if not ttmp_mat[w][h]:
                            ttmp_mat[w].pop(h)
                    while len(ttmp_mat[w]) < H:
                        ttmp_mat[w].append(0)

                check(ttmp_mat, depth+1, cnt + t_cnt) # 다음에 뭐를 터뜨릴지 다시 재귀

                break

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    org_mat = [list(map(int, input().split())) for _ in range(H)]   # 입력받은 매트릭스
    mat = [[0 for _ in range(H)] for _ in range(W)]                 # 편의를 위해 옆으로 돌릴거임
    for i in range(H):                                              # 돌려버리기
        for j in range(W):
            mat[j][-i-1]  = org_mat[i][j]

    blocks = 0              # 원래 블록 개수 세기
    for i in range(W):
        for j in range(H):
            if mat[i][j]:
                blocks += 1

    max_cnt = 0             # 맥스값 초기화
    check(mat, 0, 0)        # 함수 실행
    print('#{} {}'.format(tc, blocks - max_cnt))    # 원래 블록 수 - 터뜨린 횟수