import sys

sys.stdin = open('2050.txt')

st = input()

for i in st:
    print(ord(i)-64, end=' ')