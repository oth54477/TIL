a = ['a', 'e', 'i', 'o', 'u']
while True:
    cnt = 0
    s = input().lower()
    if s == '#':
        break
    for ss in s:
        if ss in a:
            cnt += 1
    print(cnt)
