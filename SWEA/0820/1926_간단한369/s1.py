import sys

sys.stdin = open('input.txt')

def sp_369(n):
    ret = []
    for i in range(1, n+1):
        num = str(i)
        cnt = 0
        for c in num:
            if c in li_369:
                cnt += 1
        if cnt:
            num = '-'*cnt
        ret.append(num)
    return ret


li_369 = ['3', '6', '9']
N = int(input())
print(*sp_369(N))
