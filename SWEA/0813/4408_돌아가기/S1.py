import sys

sys.stdin = open('input.txt')


def back_home(n, li):
    way = [0] * 201 # 복도
    way_max = 0
    for kid in range(n):
        start = (li[kid][0] + 1) // 2 # 홀수와 짝수방이 복도를 공유하도록 했다.
        end = (li[kid][1] + 1) // 2
        if start > end : # 움직이는 방향에 구애받지 않도록 했다.
            start, end = end, start
        for i in range(start, end + 1):
            way[i] += 1 # 지나간 경로에 1씩 더하면, 경로의 숫자 중 가장 큰 값이 반복해야할 횟수가 된다.
            if way[i] > way_max :
                way_max = way[i]
    return way_max


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(tc, back_home(N, li)))


''' 이전에 시도했던 방법, 정답보다 비효율적이긴 하지만 작동할 줄 알았는데, 주어진 샘플 테스트케이스는 통과했지만 SWEA에 제출하면 fail이 나왔다.
def back_home(n, li):
    check = [False] * n
    cnt = 0
    again = True
    while again:
        way = [False] * 201
        for kid in range(n) :
            if check[kid] :
                continue
            start = (li[kid][0] + 1) // 2
            end = (li[kid][1] + 1) // 2
            if start > end :
                start, end = end, start
            for i in range(start, end + 1):
                if way[i]:
                    break
            else :
                for k in range(start, end + 1):
                    way[k] = True
                check[kid] = True
        cnt += 1
        again = False
        for i in check:
            if not i:
                again = True

    return cnt
'''