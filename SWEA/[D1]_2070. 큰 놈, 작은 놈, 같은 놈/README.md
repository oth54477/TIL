# 2070. 큰 놈, 작은 놈, 같은 놈

- Map()함수를 활용해 여러개의 변수에 값을 저장한다.
- If-elif-else 문 이용

```python
T = int(input())

for t in range(1, T + 1):
    num1, num2 = map(int, input().split())  # 입력받은 두 수를 num1과 num2에 저장

    if num1 > num2:  # num1이 num2보다 크다면 '>'
        result = '>'
    elif num1 < num2:  # num1이 num2보다 작다면 '<'
        result = '<'
    else:  # 둘다 아니라면 '='
        result = '='

    print(f'#{t} {result}')

```

