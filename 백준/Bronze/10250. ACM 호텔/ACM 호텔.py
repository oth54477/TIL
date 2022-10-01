import sys
input = sys.stdin.readline

for t in range(int(input())):
    h, w, n = map(int, input().split())
    a = n % h
    b = n // h + 1
    result = ''
    if a == 0:
        b -= 1
        a =  h
    a, b = str(a), str(b)
    if len(b) == 2:
        result = a + b
    else:
        result = a + '0' + b
        
    print(result)



