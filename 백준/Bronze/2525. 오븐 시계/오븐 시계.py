h, m = map(int,input().split())
c = int(input())
total = h * 60 + m + c
h, m = (total // 60) % 24, total % 60
print(h, m)