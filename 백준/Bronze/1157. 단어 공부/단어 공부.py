a = input().upper()
max_cnt = 0
for i in set(map(str, a)):
    cnt = a.count(i)
    if max_cnt < cnt:
        max_cnt = cnt
        max_s = i
    elif max_cnt == cnt:
        max_s = '?'
print(max_s)