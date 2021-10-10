import sys

sys.stdin = open('input.txt')
PASSWORD = {
    '0001101': '0',
    '0011001': '1',
    '0010011': '2',
    '0111101': '3',
    '0100011': '4',
    '0110001': '5',
    '0101111': '6',
    '0111011': '7',
    '0110111': '8',
    '0001011': '9'
}
def check(bin_code):
    hol, jak, key = 0, 0, 0
    for i in range(8):
        idx = i * 7
        num = PASSWORD[bin_code[idx:idx+7]]
        if i<7:
            if not i%2:
                hol += int(num)
            else:
                jak += int(num)
        else :
            key = int(num)
    if not (hol*3 + jak + key)%10:
        return hol + jak + key
    else:
        return 0




def read(N, M):
    li = [input() for _ in range(N)]
    for y in range(N):
        for x in range(M-1, 54, -1):
            if li[y][x] == '1':
                bin_code = li[y][x-55:x+1]
                return check(bin_code)



T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, read(N, M)))