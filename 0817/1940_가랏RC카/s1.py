import sys

sys.stdin = open('input.txt')

def rcCar(n):
    moved = 0 # 움직인 위치
    drc, acc, vlc = 0, 0, 0 # 방향, 가속도, 현재속도

    for _ in range(n):
        cmd = list(map(int, input().split()))
        if cmd[0]: # 커맨드의 첫 값이 0이 아닐 때,
            drc, acc = cmd
            if drc == 1: # 가속이면
                vlc += acc # 현속도에 가속도를 더 한다
            else : # 감속이면
                vlc -= acc # 현속도에서 가속도를 뺀다.
                if vlc < 0 : # 속도가 음수이면 0으로 바꾼다.
                    vlc = 0
        moved += vlc   # 속도만큼 움직인다.
    return moved


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{} {}'.format(tc, rcCar(N)))