import sys
input = sys.stdin.readline

n = int(input().strip())
k = int(input().strip())
sensors = list(map(int, input().strip().split()))
sensors.sort()
d = []
for i in range(n-1):
    d.append(sensors[i+1] - sensors[i])
d.sort()
print(sum(d[:n-k]))
