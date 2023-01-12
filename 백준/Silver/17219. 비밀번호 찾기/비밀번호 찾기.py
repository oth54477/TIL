import sys
from collections import defaultdict
input = sys.stdin.readline

n, m = map(int, input().strip().split())

site_dict = defaultdict(str)

for _ in range(n):
    site, pw = input().strip().split()
    site_dict[site] = pw

for _ in range(m):
    find_pw = input().strip()
    print(site_dict[find_pw])