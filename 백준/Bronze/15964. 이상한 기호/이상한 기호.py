def at(A, B):
    return (A + B) * (A - B)


A, B = map(int, input().split())

print(at(A, B))
