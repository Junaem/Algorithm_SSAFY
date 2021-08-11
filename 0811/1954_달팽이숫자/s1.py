import sys

sys.stdin = open('input.txt')

def Snail(n): # 하나의 달팽이를 그리는 함수
    li = [([0] * n) for _ in range(n)] # 필요한 크기의 빈 2차원 배열
    drcs = [[0, 1], [1, 0], [0, -1], [-1, 0]] # 우하좌상 순의 방향
    drc = 0 # 현재 방향 인덱스
    cnt = 0 # 현재 적을 숫자
    now = [0, -1] # 현재 위치
    # 마지막으로 적을 숫자는 n의 제곱
    while cnt < n ** 2:
        now_plus = [now[0]+drcs[drc][0], now[1]+drcs[drc][1]] # 움직이고자 하는 위치
        # 움직일 수 있는지 확인한다.
        if 0 <= now_plus[0] < n and 0 <= now_plus[1] < n and not li[now_plus[0]][now_plus[1]] :
            now = now_plus # 움직인다
            cnt += 1 # 적을 숫자를 올린다
            li[now_plus[0]][now_plus[1]] = str(cnt) # 출력하기 편하게 str형태로 넣었다.
        else :
            drc = (drc + 1) % 4 # 못 움직이면 방향을 오른쪽으로 돌린다
    return li


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = Snail(N)
    print('#{}'.format(tc))
    for i in range(N):
        print(' '.join(li[i]))
    # 어차피 한 줄 띄워야 하기에 print를 따로 썼다.