import sys

sys.stdin = open('input.txt')

def alien(n):
    # 받아올 리스트
    nums = list(input().split())
    cnt_li = [0] * 10 # 각각의 숫자가 몇 번 쓰였는지 저장할 리스트
    # 외계숫자들
    alien_num = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    # 받은 리스트를 돌면서 각각의 숫자가 쓰인 횟수를 저장
    for num in nums :
        for idx in range(10):
            if num == alien_num[idx]:
                cnt_li[idx] += 1
                break
    ret = []
    # 각 외계숫자를 쓰인 횟수만큼 빈 리스트에 더한다.
    for i in range(10):
        ret += [alien_num[i] for _ in range(cnt_li[i])]

    return ret


T = int(input())

for _ in range(T):
    info = input().split()
    print('{}'.format(info[0]), *alien(int(info[1])))