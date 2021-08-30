import sys

sys.stdin = open('input.txt')

def ladder():
    lad = [list(map(int, input().split())) for _ in range(100)]
    now = [99, 0] # 도착지점에서 출발, x 위치는 아직 모름
    for i in range(100):
        if lad[99][i] == 2: # x 위치를 찾아서 설정
            now[1] = i
    drcs = [[-1, 0], [0, -1], [0, 1]] # 각각 위, 왼쪽, 오른쪽 방향
    drc = 0

    while now[0] > 0: # 첫째줄에 올 때까지 탐색
        if drc != 2 and now[1] > 0 and lad[now[0]][now[1]-1]:
            drc = 1 # 오른쪽으로 가고 있지 않고, 왼쪽으로 갈 수 있으면 왼쪽
        elif drc != 1 and now[1] <99 and lad[now[0]][now[1]+1]:
            drc = 2 # 왼쪽으로 가고 있지 않고, 오른쪽으로 갈 수 있으면 오른쪽
        else : # 둘 다 아니면 위로
            drc = 0
        now = [now[0] + drcs[drc][0], now[1] + drcs[drc][1]]

    return now[1]


for _ in range(10):
    t = int(input())
    print('#{} {}'.format(t, ladder()))