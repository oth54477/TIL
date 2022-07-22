# 2071. 평균값 구하기

- Sum()함수와 len()함수를 활용해 평균값을 구한다.
- Round()함수를 활용해 반올림을 한다.

```python
T = int(input())

for t in range(1, T + 1):
    numbers = list(map(int, input().split()))  # 입력을 받아서 리스트 numbers에 저장

    avr = sum(numbers) / len(
        numbers
    )  # sum()함수를 활용해 리스트 안에 있는 숫자들의 합을 구한 후, 숫자의 개수(리스트 길이)로 나눠 평균 구하기
    int_avr = round(avr)  # float형태인 avr을 반올림해 int형식으로 바꿔주기

    print(f'#{t} {int_avr}')

```



