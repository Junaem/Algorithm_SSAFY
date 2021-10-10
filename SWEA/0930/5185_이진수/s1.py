import sys

sys.stdin = open('input.txt')




T = int(input())
for tc in range(1, T+1):
    N, x_num = input().split()
    hex_len = len(x_num)

    N = int(N)
    x_num = int(x_num, 16)
    x_num = str(bin(x_num))[2:]
    cha = hex_len*4 - len(x_num)
    x_num = '0'*cha + x_num
    print('#{} {}'.format(tc, x_num))