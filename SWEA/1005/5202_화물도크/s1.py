import  sys

sys.stdin = open('input.txt')

def check(li):
    works = 0
    for w in li:
        start, end = w[0], w[1]
        for h in range(start, end):
            if not t_table[h]:
                break
        else:
            for h in range(start, end):
                t_table[h] = False
            works += 1
    return works


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    t_table = [True for _ in range(25)]
    li = []
    for _ in range(N):
        s, e = map(int, input().split())
        li.append((s, e, e-s))

    li = sorted(li, key= lambda x: x[2])
    print('#{} {}'.format(tc, check(li)))