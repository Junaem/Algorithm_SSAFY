import sys

sys.stdin = open('input.txt')

dY = [0, 1, 0, -1]
dX = [1, 0, -1, 0]

def maze_runner(y, x):
    for d in range(4):
        n_y, n_x = y + dY[d], x + dX[d]
        mov = maze[n_y][n_x]

        if mov == '3':
            return 1
        elif mov == '1':
            continue
        maze[n_y][n_x] = '1'
        if maze_runner(n_y, n_x):
            return 1
    return 0



for _ in range(10):
    tc = int(input())
    maze = [[] for _ in range(16)]
    for i in range(16):
        st = input()
        for j in st:
            maze[i].append(j)
    print('#{} {}'.format(tc, maze_runner(1, 1)))