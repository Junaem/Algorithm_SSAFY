import sys

sys.stdin = open('input.txt')

def laser_split(pipes):
    splited = '|'.join(pipes.split('()')) # split과 join을 통해 레이저를 따로 표시한다
    level = 0 # 현재 쌓여있는 파이프의 갯수
    rtn = 0 # 현재 잘라낸 파이프의 갯수
    for i in splited: # 각 자들을 돌면서
        if i == '(': # 시작점을 만나면 쌓인 파이프 +1
            level += 1
        elif i == ')': # 끝점을 만나면 파이프 -1하고, 잘려나간 끄트머리 하나를 rtn에 추가
            level -= 1
            rtn += 1
        else: # 레이저로 자를 때 현재 쌓인 파이프의 갯수만큼 rtn에 플러스
            rtn += level

    return rtn

T = int(input())

for tc in range(1, T+1):
    pipes = input()
    print('#{} {}'.format(tc,laser_split(pipes)))

