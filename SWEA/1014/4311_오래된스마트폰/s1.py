import sys

sys.stdin = open('input.txt')

def calc(num, touch):
    global min_touch
    if touch > min(min_touch-1, M): return
    if num <0 or num > 999: return
    if num == W:
        min_touch = touch+1
        return

    for n in able_nums:
        if num+n == W:
            calc(num * 10 + n, touch)
        else:
            calc(num * 10 + n, touch + 1)
        for oper in able_opers:
            if oper == 1:
                calc(num + n, touch + 2)
            elif oper == 2:
                calc(num - n, touch + 2)
            elif oper == 3:
                calc(num * n, touch + 2)
            elif oper == 4 and n!= 0:
                calc(num // n, touch + 2)




T = int(input())
for tc in range(1, T+1):
    N, O, M = map(int, input().split())
    able_nums = list(map(int, input().split()))
    able_opers = list(map(int, input().split()))
    W = int(input())
    min_touch = 1000
    calc(0, 0)
    print(min_touch)