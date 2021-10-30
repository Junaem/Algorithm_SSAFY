import sys

sys.stdin = open('input.txt')

def tower(height, idx_st):
    global min_able

    if B <= height:
        if height < min_able:
            min_able = height
        return

    for idx in range(idx_st, N):       # 인덱스가 N-1일때 idx_st로 넘어오면 여기서 range(N,N)이 돼서 에러 안 나는듯
        tower(height+heights[idx], idx+1)



T = int(input())
for tc in range(1,T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    min_able = sum(heights)
    tower(0, 0)
    print('#{} {}'.format(tc, min_able-B))