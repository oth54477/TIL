table = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4, '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}
for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    for _ in range(n):
        line = input()
        if int(line) != 0:
            real_line = line
    line = real_line.strip('0')
    line = ('0' * (7 - (len(line) % 7))) + line
    cnt, chk, result = 0, 0, 0
    for i in range(0, len(line), 7):
        cnt += 1
        num = table[line[i : i + 7]]
        if cnt % 2 == 0:
            chk += num
        else:
            chk += num * 3
        result += num
    if chk % 10 != 0:
        result = 0
    print(f'#{t} {result}')
