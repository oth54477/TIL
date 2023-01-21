import sys
from heapq import heappop, heappush
input = sys.stdin.readline

n = int(input().strip())
class_list = [list(map(int, input().strip().split())) for _ in range(n)]
class_list  .sort()
room = []
heappush(room, class_list[0][1])
for i in range(1, n): 
    if class_list[i][0] < room[0]:
        heappush(room, class_list[i][1])
    else:
        heappop(room)
        heappush(room, class_list[i][1])
print(len(room))


