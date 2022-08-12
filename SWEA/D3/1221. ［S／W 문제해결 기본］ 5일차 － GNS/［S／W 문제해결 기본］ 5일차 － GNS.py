table = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
for t in range(1, int(input()) + 1):
    tc, n = map(str, input().split())
    arr = input().split()

    cnt_arr = [0] * 10
    for idx, word in enumerate(table):
        cnt_arr[idx] += arr.count(word)

    print(tc)
    for i in range(10):
        print((table[i] + ' ') * cnt_arr[i], end='')
