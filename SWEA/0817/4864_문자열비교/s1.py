import sys

sys.stdin = open('input.txt')


def str_compare(st1, st2):
    len1 = len(st1)
    len2 = len(st2)

    for i in range(len2-len1+1): # 비교를 시작할 위치
        for k in range(len1): # 각 글자를 비교
            if st1[k] != st2[i+k]: # 다른 글자가 있으면 break
                break
        else : # k for문을 다 돌아도 다른 글자가 없으면 결과를 찾았으므로 return 1
            return 1

    return 0


T = int(input())

for tc in range(1, T + 1):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(tc, str_compare(str1, str2)))