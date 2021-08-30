import sys

sys.stdin = open('input.txt')

pri_out = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 3, ')': -1} # oper 바깥에 있을 때 우선순위, in-coming priority라고 하더라
pri_in = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0, ')': -1} # oper 안에 있을 때 우선순위, in-stack prioriyty라고 한다.


def to_infix(st): # 중위식을 후위식으로 바꾸는 함수
    oper = [] # 연산자들을 저장할 스택 리스트
    rtn = [] # 후위식으로 만들어 리턴할 리스트

    for c in st: # 각 스트링의 글자에 대해
        if '0' <= c <= '9': # 숫자 범위면
            rtn.append(int(c)) # 숫자로 rtn에 저장
        elif c == ')': # 닫는 괄호면
            while oper[-1] != '(': # 여는 괄호를 만날 때까지 oper의 모든 연산자를 rtn에 옮기고
                rtn.append(oper.pop())
            oper.pop() # 여는 괄호를 없앤다.
        else: # 그 외 연산자면
            while oper and pri_out[c] <= pri_in[oper[-1]]: # c의 icp가 oper에 쌓인 연산자의 isp보다 높지 않으면
                rtn.append(oper.pop()) # 다 rtn에 옮긴다.
            oper.append(c) # 이후 opr에 c를 넣는다

    if oper: # 이 과정이 끝나고 oper이 남아있으면
        rtn.append(oper[::-1]) # 거꾸로 돌려서 rtn에 합친다
    return rtn # 후위식이 된 rtn을 리턴


def calc(infix): # 후위식을 계산하는 함수
    numbers = [] # 피연산자들의 리스트
    for ele in infix: # infix의 원소들을 순회하며
        if ele in pri_in: # 원소가 연산자면
            b = numbers.pop() # 숫자 두 개를 거꾸로 꺼내어
            a = numbers.pop()

            if ele == '+': # 알맞은 연산을 하여 rslt에 저장
                rslt = a + b
            elif ele == '-':
                rslt = a - b
            elif ele == '*':
                rslt = a * b
            else:
                rslt = a // b 
        else: # 그렇지 않으면(= 숫자면)
            rslt = ele # 원소를 rslt에 저장
        numbers.append(rslt) # rslt를 피연산자 리스트에 넣는다.
    return numbers.pop() # 마지막에 남은 값이 계산 결과


for tc in range(1, 11):
    N = input() # 안 쓸거니까 그냥 받아만 놓는다.
    st = input() # 입력된 str
    infix = to_infix(st) # str을 후위식으로 바꾸고
    print('#{} {}'.format(tc, calc(infix))) # 계산