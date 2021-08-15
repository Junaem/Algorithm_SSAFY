import sys

sys.stdin = open('1545.txt')

N = int(input())

for i in range(N, -1, -1):
    print(i, end=' ')