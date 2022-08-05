x = int(input())  # 원하는 길이 xcm
bars = [64]  # 원래 가지고있는 막대의 길이 64cm

while True:
    sum_bars = sum(bars)
    if sum_bars > x:  # x보다 가지고 있는 막대기의 합이 큰 경우
        half_bar = int(bars.pop() / 2)  # 제일 짧은 것을 절반으로 자른다.
        bars.append(half_bar)  # 하나는 버리고 나머지 하나는 막대기 목록에 추가한다.
        if sum(bars) < x:  # 막대기들의 합이 x보다 작으면
            bars.append(half_bar)  # 버린 반절을 추가한다
    else:   # 이외의 경우에는 막대가 몇개 필요한지 출력한다.
        print(len(bars))
        break