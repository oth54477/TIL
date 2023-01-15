import sys
input = sys.stdin.readline

n = int(input().strip())
tips = [int(input().strip()) for _ in range(n)]

tips.sort(reverse=True)
result = 0
for idx, tip in enumerate(tips):
    real_tip = tip - (idx)
    if real_tip > 0:
        result += tip - (idx)
print(result)
