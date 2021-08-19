import sys

sys.stdin = open('input.txt')

# 처음에는 슬라이싱을 안하고 pw를 list로 만들어서 pop을 사용했는데, 비교해보니 속도 차이가 크지 않았다.
def password(n, nums): # nums는 그냥 String으로 받아왔다.
    pw = ''  # 출력할 비밀번호
    for i in nums: # 문자열의 각 숫자(글자)가
        if pw and pw[-1] == i: # pw가 비어있지 않을때, 이전 글자와 같다면
            pw = pw[:-1] # 이전 글자를 없앤다.
        else : # 그 외의 경우에는
            pw += i # 패스워드에 더한다.
    return pw


for tc in range(1, 11):
    N, nums = input().split()
    print('#{} {}'.format(tc, password(int(N), nums)))