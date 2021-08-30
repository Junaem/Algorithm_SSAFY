import sys

sys.stdin = open('input.txt')

dY = [0, 1, 0, -1]
dX = [1, 0, -1, 0]

def maze_runner():
    stack = [(1, 1)]
    while stack:
        y, x = stack.pop()

        for d in range(4):
            n_y, n_x = y + dY[d], x + dX[d]
            mov = maze[n_y][n_x]

            if mov == '3':
                return 1
            elif mov == '1':
                continue
            else :
                maze[n_y][n_x] = '1'
                stack.append((n_y, n_x))


    return 0



for _ in range(10):
    tc = int(input())
    maze = [[] for _ in range(100)]
    for i in range(100):
        st = input()
        for j in st:
            maze[i].append(j)
    print('#{} {}'.format(tc, maze_runner()))