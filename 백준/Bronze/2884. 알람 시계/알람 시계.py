h, m = map(int,input().split())
time = h * 60 + m - 45
print((time//60) % 24, time%60)