# 2007. 패턴 마디의 길이

for t in range(1, int(input()) + 1):
    s = input()
    min_s = 30
    min_idx = 0
    for i in range(11):
        new_s = s.replace(s[:i], '')
        if min_s > len(new_s):
            min_s = len(new_s)
            min_idx = i

    print(f'#{t} {min_idx}')
