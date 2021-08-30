import sys

sys.stdin = open('input.txt')

moems = ['a', 'e', 'i', 'o', 'u']
def no_moem(st):
    ret = ''
    for c in st:
        if not c in moems:
            ret += c
    return ret


T = int(input())
for tc in range(1, T+1):
    st = input()
    print('#{} {}'.format(tc, no_moem(st)))