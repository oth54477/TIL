# 2068. 최대수 구하기

- Max()함수를 활용해 리스트에서 가장 큰 값을 구한다.
  - max(iterable, *[, default=obj, key=func])
  - min(iterable, *[, default=obj, key=func])

```python
T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int, input().split()))
    # max()함수를 이용해 리스트 numbers에서 가장 큰 값을 변수 max_number에 저장
    max_number = max(numbers)  

    print(f'#{t} {max_number}')

```

