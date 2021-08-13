import sys

sys.stdin = open('input.txt', 'rt', encoding='UTF8')

def Calc(wd, st):
    wd_l = len(wd)
    st_l = len(st)
    cnt = 0

    for i in range(st_l - wd_l):
        for k in range(wd_l):
            if not st[i+k] == wd[k]:
                break
        else :
            cnt += 1
    return cnt


for tc in range(1, 11):
    wd = input()
    st = input()
    print('#{} {}'.format(tc, Calc(wd, st)))
