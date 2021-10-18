import sys

sys.stdin = open('input.txt')

def group(n, m, lst):
    sets= [{i} for i in range(1, N+1)]

    for i in range(m):
        a, b = lst[i*2], lst[i*2+1]

        s1i =-1
        while s1i < len(sets):
            s1i+=1
            s1 = sets[s1i]
            if a in s1:
                for s2i in range(len(sets)):
                    s2 = sets[s2i]
                    if b in s2 :
                        if s2i != s1i:
                            sets[s1i] = s1.union(s2)
                            sets.pop(s2i)

                        break
                break

    return len(sets)


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    print('#{} {}'.format(tc, group(N, M, lst)))