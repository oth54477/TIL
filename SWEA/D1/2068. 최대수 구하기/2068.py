T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int, input().split()))

    max_number = max(numbers)  # max()함수를 이용해 리스트 numbers에서 가장 큰 값을 변수 max_number에 저장

    print(f'#{t} {max_number}')
