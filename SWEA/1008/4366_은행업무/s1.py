import sys

sys.stdin = open('input.txt')

dict2 = {'0': [1], '1': [-1]}
dict3 = {'0': [+1, +2],
         '1': [-1, +1],
         '2': [-2, -1]
         }

def check(n2, n3):
    n2_set = set()
    n3_set = set()
    n2_10 = int(n2, 2)
    n3_10 = int(n3, 3)

    for t in range(len(n2)):
        scale = 2 ** (len(n2)-1-t)
        for plus in dict2[n2[t]]:
            n2_set.add(n2_10 + plus*scale)

    for t in range(len(n3)):
        scale = 3 ** (len(n3)-1-t)
        for plus in dict3[n3[t]]:
            n3_set.add(n3_10 + plus*scale)

    return (n2_set - (n2_set- n3_set)).pop()

T = int(input())
for tc in range(1, T+1):
    n2 = input()
    n3 = input()
    print('#{} {}'.format(tc, check(n2, n3)))