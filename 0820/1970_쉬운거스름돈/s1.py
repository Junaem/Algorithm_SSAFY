import sys

sys.stdin = open('input.txt')

cur = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

def changes(money):
    li = [0] * 8

    for i in range(8):
        li[i] = money // cur[i]
        money = money % cur[i]

    return li


T = int(input())
for tc in range(1, T+1):
    money = int(input())
    print('#{}'.format(tc))
    print(*changes(money))