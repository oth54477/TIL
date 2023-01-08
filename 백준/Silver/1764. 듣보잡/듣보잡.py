import sys

input = sys.stdin.readline

n, m = map(int, input().strip().split())
n_arr = {input().strip() for _ in range(n)}
m_arr = {input().strip() for _ in range(m)}
result = set()
for name in n_arr:
    if name in m_arr:
        result.add(name)

print(len(result),*sorted(result), sep='\n')