import sys
import math
input = sys.stdin.readline

a, b, v = list(map(int, input().split()))

print(math.ceil((v-b) / (a - b)))
