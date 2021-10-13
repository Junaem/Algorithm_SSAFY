import sys

sys.stdin = open('input.txt')

def move(conts, trucks):
    answer = 0
    for truck in trucks:
        for i in range(len(conts)-1, -1, -1):
            cont = conts.pop()
            if cont <= truck:
                answer += cont
                break
    return answer


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    conts = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())), reverse=True)

    print('#{} {}'.format(tc, move(conts, trucks)))