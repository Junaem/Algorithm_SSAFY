import sys

sys.stdin = open('input.txt')

# K와 N을 입력받아 테스트 케이스 하나를 수행하는 함수
def bus_func(k, n):
    # way는 목적지 까지의 길, 충전소가 있으면 True값을 준다.
    way = [False] * (n+1)
    chargers = list(map(int, input().split()))

    for charger in chargers:
        way[charger] = True
    #버스는 현재의 위치, charges는 충전 횟수
    bus = 0
    charges = 0
    #버스는 return을 만날때 까지 달린다.
    while True:
        # 갈 수 있는 가장 먼 충전소부터 가까운 곳 순으로 탐색
        for idx in range(bus + k, bus, -1):
            if idx >= n:    # n 이상 먼 곳에 갈 수 있으면 충전횟수를 리턴하고 탐색 종료
                return charges
            if way[idx]: # 먼 충전소를 찾으면 현재 위치를 그곳으로 옮기고 충전횟수 +1
                bus = idx
                charges += 1
                break
        else : # 현재 위치 앞까지 탐색해도 충전소가 없었다면 0 리턴, 함수 종료
            return 0



T = int(input())

for i in range(T):
    K, N, M = map(int, input().split())
    print('#{} {}'.format(i+1, bus_func(K, N)))
