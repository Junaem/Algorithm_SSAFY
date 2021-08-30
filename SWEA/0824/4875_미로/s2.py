import sys

sys.stdin = open('input.txt')

dlt = [[1, 0], [0, 1], [-1, 0], [0, -1]] # 움직일 방향들


def maze_runner(b, a): # 얘는 스택으로
    stack = [[b, a]] # 일단 시작 위치를 스택에 넣어둔다.
    while stack:
        y, x = stack.pop() # stack에서 값을 pop하여 위치로 사용
        for i in range(4): # 하, 우, 상, 좌 의 순서로 돈다.
            dy, dx = dlt[i] # 방향을 꺼내와서
            ny, nx = y + dy, x + dx # 새로운 좌표를 만든다.

            if not (0 <= ny < N and 0 <= nx < N): # 그 좌표가 유효한 지 확인
                continue

            nxt_p = maze[ny][nx] # 유효하다면 그 maze의 그 좌표 값 확인

            if nxt_p == 3: # 3이면 도착
                return 1
            elif nxt_p == 1: # 1이면 무시
                continue
            maze[ny][nx] = 1 # 아니라면 방문 표시를 해두고
            stack.append([ny, nx]) # stack에 넣는다.
    return 0


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [[] for _ in range(N)]
    s_y, s_x = 0, 0

    for i in range(N):
        st = input()
        for j in range(N):
            maze[i].append(int(st[j]))
            if st[j] =='2':
                s_y, s_x = i, j

    print('#{} {}'.format(tc,maze_runner(s_y, s_x)))