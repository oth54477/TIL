import sys

input = sys.stdin.readline

calculation = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '*': lambda x, y: x * y,
    '/': lambda x, y: x / y
}

n = int(input())
string = input().strip()

alpas = list(map(chr, range(65, 65+n)))
nums = [int(input()) for _ in range(n)]
table = dict(zip(alpas, nums))

expression = list(map(lambda x: table[x] if x in table else x, string))
temp = []
for e in expression:
    if type(e) is int:
        temp.append(e)
    else:
        y = temp.pop()
        x = temp.pop()
        temp.append(calculation[e](x, y))


print(f'{temp[0]:.2f}')
 