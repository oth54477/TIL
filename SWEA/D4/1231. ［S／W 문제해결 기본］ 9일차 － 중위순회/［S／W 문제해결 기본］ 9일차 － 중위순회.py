def inorder(n):
    global result
    g = graphs[n]
    if not g:
        result += nodes[n]
    else:
        inorder(g[0])
        result += nodes[n]
        if len(g) == 2:
            inorder(g[1])


for t in range(1, 11):
    E = int(input())
    nodes = [0] * (E + 1)
    graphs = [[] for _ in range(E + 1)]
    for _ in range(E):
        num, node, *graph = map(lambda x: int(x) if x.isdigit() else str(x), input().split())
        nodes[num] = node
        graphs[num] = graph
    V = E + 1
    root, result = 1, ''
    inorder(root)
    print(f'#{t} {result}')