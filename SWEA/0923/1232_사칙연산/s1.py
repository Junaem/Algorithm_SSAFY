import sys

sys.stdin = open('input.txt')

<<<<<<< HEAD
operators = '+-*/'

def calc(node):
    if str(tree[node][0]) not in operators:
=======
calculators = '+-*/'

def calc(node):
    if str(tree[node][0]) not in calculators:
>>>>>>> 80b45840e22dc7ff75df0b380c13db71775a85df
        return tree[node][0]

    a = calc(tree[node][1])
    b = calc(tree[node][2])
<<<<<<< HEAD
    operator = tree[node][0]
    result = 0

    if operator == '+':
        result = a + b
    elif operator == '-':
        result = a - b
    elif operator == '*':
        result = a * b
    elif operator == '/':
=======
    calculator = tree[node][0]
    result = 0

    if calculator == '+':
        result = a + b
    elif calculator == '-':
        result = a - b
    elif calculator == '*':
        result = a * b
    elif calculator == '/':
>>>>>>> 80b45840e22dc7ff75df0b380c13db71775a85df
        result = a / b

    return result

for tc in range(1, 11):
    N = int(input())
    tree = [[] for _ in range(N+1)]
    for _ in range(N):
        inp = list(input().split())
        idx = int(inp[0])
<<<<<<< HEAD
        if inp[1] in operators:
=======
        if inp[1] in calculators:
>>>>>>> 80b45840e22dc7ff75df0b380c13db71775a85df
            tree[idx].append(inp[1])
            tree[idx].append(int(inp[2]))
            tree[idx].append(int(inp[3]))
        else:
            tree[idx].append(int(inp[1]))
<<<<<<< HEAD
    print(tree)
=======
>>>>>>> 80b45840e22dc7ff75df0b380c13db71775a85df
    print('#{} {}'.format(tc, int(calc(1))))