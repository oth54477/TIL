table = {
    "211": "0",
    "221": "1",
    "122": "2",
    "411": "3",
    "132": "4",
    "231": "5",
    "114": "6",
    "312": "7",
    "213": "8",
    "112": "9",
}


def find_ratio():
    global binary
    i_0 = binary.index('0')
    binary = binary[i_0:]
    i_1 = binary.index('1')
    binary = binary[i_1:]
    if '0' in binary:
        i_00 = binary.index('0')
    else:
        i_00 = len(binary)
    ratio = [i_0, i_1, i_00]
    binary = binary[i_00:]
    return ratio

answer = []
for t in range(1, int(input()) + 1):
    n, m = map(int, input().split())
    lines = set()
    for _ in range(n):
        line = input()[:m].strip()
        if not line.isnumeric():
            lines.add(line.strip('0'))

    codes = set()
    for line in lines:
        binary = format(int(line, 16), 'b')
        binary = binary.strip('0')
        code = ''
        while binary:
            ratio = find_ratio()
            min_num = min(ratio)
            a, b, c = map(lambda x: str(x//min_num), ratio)
            ratio = a+b+c
            code += table[ratio]
            binary = binary.strip('0')
            if len(code) == 8:
                codes.add(code)
                code = ''
    result = 0
    for code in codes:
        chk_num, sum_num = 0, 0
        for idx, num in enumerate(code):
            num = int(num)
            if idx % 2 == 0:
                chk_num += num * 3
            else:
                chk_num += num
            sum_num += num
        if chk_num % 10 == 0:
            result += sum_num
    answer.append(f'#{t} {result}')
    # print(f'#{t} {result}')
print(*answer,sep='\n')