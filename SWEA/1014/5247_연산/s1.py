import sys
from collections import deque

sys.stdin = open('input.txt')

def calc(N, cnt, M):
    min_calc = 1000000
    q = deque([N])
    num_dic = {N: 0}
    while q:
        num = q.popleft()
        cnt =  num_dic[num]
        if num == M: return cnt
        if num > min(M+10, 1000000): continue

        if num+1 not in num_dic:
            num_dic[num+1] = cnt+1
            q.append(num+1)
        if num-1 not in num_dic:
            num_dic[num-1] = cnt+1
            q.append(num-1)
        if num*2 not in num_dic:
            num_dic[num*2] = cnt+1
            q.append(num*2)
        if num-10 not in num_dic:
            num_dic[num-10] = cnt+1
            q.append(num-10)





T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())

    print('#{} {}'.format(tc, calc(N, 0, M)))