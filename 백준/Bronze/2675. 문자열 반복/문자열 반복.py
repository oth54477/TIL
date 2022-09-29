for t in range(int(input())):
    n, s = map(str, input().split())
    n = int(n)
    result = ''
    for i in s:
        result += (i * n)
    print(result)