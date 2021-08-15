import sys

sys.stdin = open('input.txt')

def bus_stop():
    N = int(input()) # 버스의 갯수
    cnt_li = [0] * 5001 # 각 정류장을 인덱스로 지나가는 버스의 수를 담을 리스트
    for i in range(N):
        a, b = map(int, input().split())
        for k in range(a, b+1): # 
            cnt_li[k] += 1
    P = int(input())
    ret = []
    for i in range(P):
        c = int(input())
        ret.append(cnt_li[c])
    return ret


T = int(input())

for tc in range(1, T+1):
    print('#{}'.format(tc), *bus_stop())