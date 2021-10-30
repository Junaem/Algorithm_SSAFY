import sys

sys.stdin = open('input.txt')

def cases(idx, cnt, table):
    if cnt == N//2:
        sums.append(check(used))
        return
    for i in range(idx+1, N):
        if i not in used:
            used.append(i)
            cases(i, cnt+1, table)
            used.pop()

def check(used):
    no_used = []
    for i in range(N):
        if i not in used:
            no_used.append(i)
    Asum, Bsum = 0, 0
    for i in range(N//2-1):
        for j in range(i+1, N//2):
            Asum += table[used[i]][used[j]] + table[used[j]][used[i]]
            Bsum += table[no_used[i]][no_used[j]] + table[no_used[j]][no_used[i]]

    return abs(Asum-Bsum)



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    used = []
    sums = []
    cases(0, 0, table)
    sums.sort()
    print('#{} {}'.format(tc, sums[0]))