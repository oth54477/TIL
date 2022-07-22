# 2056. 연월일 달력

- 31일까지 있는 날과 30일, 28일이 있는 날을 분리해 확인
- 문자열 슬라이싱 사용

```python
T = int(input())

for t in range(1, T + 1):
    number = input()
    month_31 = ['01', '03', '05', '07', '08', '10', '12']   # 31일까지 있는 달
    month_30 = ['04', '06', '09', '11']     # 30일까지 있는 달
    month_28 = ['02']       # 28일까지 있는 달
    if number[4:6] in month_31 and 1 <= int(number[6:8]) <= 31:
        date = f'{number[0:4]}/{number[4:6]}/{number[6:8]}'
    elif number[4:6] in month_30 and 1 <= int(number[6:8]) <= 30:
        date = f'{number[0:4]}/{number[4:6]}/{number[6:8]}'
    elif number[4:6] in month_28 and 1 <= int(number[6:8]) <= 28:
        date = f'{number[0:4]}/{number[4:6]}/{number[6:8]}'
    else:
        date = -1
    print(f'#{t} {date}')
```



