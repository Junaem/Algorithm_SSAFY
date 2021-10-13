import sys

sys.stdin = open('input.txt')

def posbl(person, perc):
    global max_perc

    if perc < max_perc:
        return
    if person == N-1:
        max_perc = perc
        return

    for task in range(N):
        if not done[task]:
            done[task] = True
            posbl(person+1, perc*table[person][task]/100)
            done[task] = False



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    done = [False for _ in range(N)]
    max_perc = 0
    posbl(-1, 100)
    print('#{} {:.6f}'.format(tc, max_perc))