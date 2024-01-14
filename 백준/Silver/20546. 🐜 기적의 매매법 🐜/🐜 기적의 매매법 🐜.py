import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

money_bnp = N   
count_bnp = 0

money_timing = N
count_timing = 0

for num, price in enumerate(arr):
    # 준현
    count_bnp += (money_bnp // price)
    money_bnp %= price

    # 성민
    temp = arr[num:num+4]

    if len(temp) < 4:
        continue

    if temp[0] < temp[1] < temp[2] < temp[3] and count_timing > 0:
        money_timing += (count_timing * temp[3])
        count_timing = 0
    elif temp[0] > temp[1] > temp[2] > temp[3]:
        count_timing += (money_timing // temp[3])
        money_timing %= temp[3]

answer_bnp = money_bnp + count_bnp * arr[-1]
answer_timing = money_timing + count_timing * arr[-1] 

if answer_bnp < answer_timing:
    print("TIMING")
elif answer_bnp > answer_timing:
    print("BNP")
else:
    print("SAMESAME")