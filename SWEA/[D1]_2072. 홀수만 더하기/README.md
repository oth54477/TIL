# 2072. 홀수만 더하기

- % 연산자를 활용해 홀수 여부를 확인한다.
- 홀수라면 더하고, 짝수라면 넘긴다.

```python
T = int(input())                    

for t in range(1, T + 1):                           # test케이스 개수 T만큼 반복
    numbers = list(map(int, input().split()))       # 입력을 받아서 리스트 numbers에 저장
    sum_value = 0                                   # 결과값으로 사용할 변수 0으로 선언
    for number in numbers:                          # 리스트 numbers에 있는 요소들을 변수 number에 차례로 대입 
        if number % 2 != 0:                         # number가 홀수인지 확인
            sum_value += number                     # 홀수라면 sum_value에 더해주기
        else:                                       # 아닐경우는 pass
            pass
    print(f'#{t} {sum_value}')

```

