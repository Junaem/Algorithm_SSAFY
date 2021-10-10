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


def find():
    codes = []
    for _ in range(N):
        r = list(input())
        for i in range(M):
            if r[i] != '0':


        idx = M-1
        sp = r.split('0000')
        for i in sp:
            a=i
            if i and i.strip('0'):
                i = str(bin(int(i, 16)))[2:].strip('0')
                if i not in codes:
                    codes.append(i)
                    if tc == 14:
                        print(len(i)%56, a, i)
                        print(r)
                        print()
    return calc(codes)


def calc(codes):
    codes_sum = 0
    for code in codes:
        size = (len(code))//56 +1
        zeros = size*56 - len(code)
        code = '0'*zeros + code

        l_size = size * 7
        hol, jak, key = 0, 0, 0
        for i in range(8):
            idx = i*7*size
            word = ''
            for k in range(7):
                word += code[idx + k*size]
            num = PASSWORD[word]
            if i == 7:
                key = int(num)
            else:
                if i%2 == 0:
                    hol += int(num)
                else:
                    jak += int(num)

        if not (hol*3 + jak+ key)%10:
            codes_sum += hol+jak+key

    return codes_sum


T= int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    print('#{} {}'.format(tc, find()))