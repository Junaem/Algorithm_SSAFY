import sys

sys.stdin = open('input.txt')


def typing(a, b):
    a_len, b_len = len(a), len(b)
    b_used = 0
    idx = 0
    # b가 몇 번 쓰였는지 검사
    while idx < a_len - b_len + 1: # 검사를 시작할 위치
        for k in range(b_len): # 위치부터 b의 길이 까지 검사
            if a[idx+k] != b[k]: # 다른 글자가 있으면 break하고 다음 idx 검사
                idx += 1
                break
        else: # 끝까지 다 같다면 b 사용량을 1올리고 idx를 b의 길이만큼 +
            b_used += 1
            idx += b_len
    # a의 길이에서 b로 생략한 입력만큼 뺀다.
    return a_len - b_used * (b_len - 1)


T = int(input())

for tc in range(1, T+1):
    A, B = input().split()
    print('#{}'.format(tc), typing(A, B))