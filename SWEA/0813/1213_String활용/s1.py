import sys

sys.stdin = open('input.txt', 'rt', encoding='UTF8')
# 찾을 단어와 전체 문자열을 인자로 받는다.
def Calc(wd, st):
    wd_l = len(wd)
    st_l = len(st)
    cnt = 0 # 단어를 찾은 횟수
    # i는 문자열 길이에서 단어의 길이를 뺀 곳(시작점)
    for i in range(st_l - wd_l + 1):
        for k in range(wd_l): # k는 단어의 n번째 글자
            if not st[i+k] == wd[k]:
                break  # 비교하여 같지 않으면 브레이크
        else: # 단어의 길이만큼 다 돌았으면 cnt +1
            cnt += 1

    return cnt


for _ in range(10):
    tc = input()
    wd = input()
    st = input()
    print('#{} {}'.format(tc, Calc(wd, st)))
