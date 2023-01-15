import sys
input = sys.stdin.readline

n = int(input().strip())
roads = list(map(int, input().strip().split()))
oils = list(map(int, input().strip().split()))

tank = 0
now = 0
result = 0
while now < n:
    now_price = oils[now]
    i = 1
    while now+i  < n:
        if oils[now + i] < now_price:
            distance = sum(roads[now:now+i])
            result += now_price * distance
            now += i
            break
        i += 1
    else:
        distance = sum(roads[now:now+i-1])
        result += now_price * distance
        now += i

print(result)