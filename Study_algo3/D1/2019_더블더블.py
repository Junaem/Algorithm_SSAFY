import sys

sys.stdin = open('2019.txt')

N = int(input())

for i in range (N + 1):
    print(2 ** i, end=' ')