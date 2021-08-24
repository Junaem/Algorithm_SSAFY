import sys

sys.stdin = open('input.txt')

def unzip(n):
    inline = ''
    for i in range(n):
        st, j = input().split()
        inline += st * int(j)
    rtn = ''
    for i in range(0, len(inline), 10):
        rtn += '\n' + inline[i:i+10]
    return rtn


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    print('#{}{}'.format(tc,unzip(N)))