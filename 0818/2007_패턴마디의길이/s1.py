import sys

sys.stdin = open('input.txt')

def repeat(st):
    for re_lang in range(1, 11): # 반복 마디의 길이를 1부터 10까지 써본다.
        for idx in range(30): # 전체 문자열의 각 글자들
            if st[idx % re_lang] != st[idx]: # idx를 길이로 나눈 나머지의 글자와, 그냥 idx가 계속 같으면 반복이다.
                break # 아닐 경우 break
        else : # 끝까지 break가 안 걸렸으면 그 길이를 리턴
            return re_lang


T = int(input())
for tc in range(1, T+1):
    st = input()
    print('#{} {}'.format(tc, repeat(st)))