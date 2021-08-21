import sys

sys.stdin = open('input.txt')

def turn_list(li, n):
    new_li = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_li[i][j] = li[n-j-1][i]
    return new_li



def three_turn(n):
    li = [list(input().split()) for _ in range(n)]
    li_turn = [[],[],[]]
    li_turn[0] = turn_list(li, n)
    li_turn[1] = turn_list(li_turn[0], n)
    li_turn[2] = turn_list(li_turn[1], n)

    ret = ''
    for i in range(n):
        ret += '\n'
        for turned_li in li_turn:
            ret += ''.join(turned_li[i]) + ' '
    return ret


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{}{}'.format(tc, three_turn(N)),)
