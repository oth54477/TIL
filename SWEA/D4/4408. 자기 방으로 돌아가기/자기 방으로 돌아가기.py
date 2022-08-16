for t in range(1, int(input()) + 1):
    n = int(input())
    paths = [0] * 201
    for _ in range(n):
        start, end = map(int, input().split())

        if start % 2 == 0:
            start_path = start // 2
        else:
            start_path = start // 2 + 1
        if end % 2 == 0:
            end_path = end // 2
        else:
            end_path = end // 2 + 1

        for idx in range(min(start_path, end_path), max(start_path, end_path) + 1):
            paths[idx] += 1

    print(f'#{t} {max(paths)}')