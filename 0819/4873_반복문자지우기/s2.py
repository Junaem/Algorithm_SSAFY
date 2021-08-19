import sys

sys.stdin = open('input.txt')

def puyopuyo(st): # 아무리 생각해도 이게 진짜 정답이다. s1은 거짓된 풀이이다.
    changed = True
    ret = st # 이 문제에선 불필요하겠지만, 안정성을 위해 st를 복사하여 사용한다.
    while changed: # 더 이상 변하지 않을 때까지 실행
        changed = False
        for i in range(len(ret) - 1): # 마지막 전까지의 글자를 돌며
            if ret[i] == ret[i+1]: # 그 글자가 다음 글자와 같으면
                target = ret[i] # 그 글자를 타겟으로 삼고
                cnt = 0 # 카운트를 셀 것이다.
                for j in range(len(ret)-i):
                    if ret[i+j] == target: # 글자가 같은 동안 카운트를 세고
                        cnt += 1
                    else : # 다른 글자가 나오면 카운트를 멈춘다.
                        break
                ret = ret[:i] + ret[i+cnt:] # 카운트한 부분을 잘라낸다.
                changed = True # 변화가 있었음을 표시하고,
                break # while 문을 다시 시작한다.
    return len(ret)




T = int(input())
for tc in range(1, T+1):
    st = input()
    print(puyopuyo(st))