def ter(n):
    result = ''
    while n != 0:
        n, r = divmod(n, 3)
        result += str(r)
    return result[::-1]


for t in range(1, int(input()) + 1):
    binary = input()
    ternary = input()
    b_decimal = int(binary, 2)
    t_decimal = int(ternary, 3)
    ter_len = len(ternary)
    bins = [b_decimal ^ 1 << i for i in range(len(binary))]
    for b in bins:
        ter_str = ter(b)
        ter_str = '0' * (ter_len - len(ter_str)) + ter_str
        cnt = 0
        for idx in range(ter_len):
            if ternary[idx] != ter_str[idx]:
                cnt += 1
        if cnt == 1:
            result = b
            break

    print(f'#{t} {result}')