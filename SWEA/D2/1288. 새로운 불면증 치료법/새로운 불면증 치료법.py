for t in range(1, int(input()) + 1):
    n = int(input())

    chk_num = set()

    k = 1
    while len(chk_num) < 10:
        kn = k * n
        str_kn = str(kn)
        for i in str_kn:
            chk_num.add(i)
        k += 1
    print(f'#{t} {kn}')