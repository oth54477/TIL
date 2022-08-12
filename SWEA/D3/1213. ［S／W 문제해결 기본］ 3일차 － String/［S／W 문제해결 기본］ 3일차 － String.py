for _ in range(10):
    t = int(input())
    find_text = input()
    text = input()

    cnt = text.count(find_text)
    print(f'#{t} {cnt}')
