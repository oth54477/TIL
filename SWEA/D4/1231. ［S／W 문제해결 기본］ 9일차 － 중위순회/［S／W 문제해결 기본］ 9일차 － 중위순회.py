def inorder(n):
    global result
    if n:
        inorder(ch1[n])
        result += nodes[n]
        inorder(ch2[n])


for t in range(1, 11):
    E = int(input())
    nodes = [0] * (E + 1)
    graphs = [[] for _ in range(E + 1)]
    for _ in range(E):
        num, node, *graph = map(
            lambda x: int(x) if x.isdigit() else str(x), input().split()
        )
        nodes[num] = node
        graphs[num] = graph
    V = E + 1
    root = 1
    ch1 = [0] * (V + 1)
    ch2 = [0] * (V + 1)
    result = ''
    for idx, value in enumerate(graphs):
        if value:
            ch1[idx] = value.pop(0)
            if value:
                ch2[idx] = value.pop(0)

    inorder(root)
    print(f'#{t} {result}')