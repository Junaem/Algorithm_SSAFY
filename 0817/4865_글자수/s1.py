import sys

sys.stdin = open('input.txt')


def str_compare(st1, st2):
    st_dic = {i:0 for i in st1} # st1의 글자들로 딕셔너리를 만들었다.
    for i in st2: # 비교할 st2의 글자
        if st_dic.get(i) != None: # 글자가 딕셔너리에 있다면
            st_dic[i] += 1 # 딕셔너리에 1을 더 한다
             
    return max(st_dic.values()) # 밸류 중 max를 리턴

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(tc, str_compare(str1, str2)))