import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = float(input())
    k = 0.5
    bin_n = ''
    for _ in range(12):
        if N >= k:
            N -= k
            bin_n += '1'
        else:
            bin_n += '0'
        k /= 2
    if N:
        bin_n = 'overflow'
    else:
        bin_n = bin_n.rstrip('0')

    print('#{} {}'.format(tc, bin_n))