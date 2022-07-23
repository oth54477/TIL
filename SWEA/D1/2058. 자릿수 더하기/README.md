# 2058. 자릿수 더하기

- string도 iterable
- For s in string: 을 하면 s에 sting의 요소를 차례로 대입

```python
N = input()
res = 0
for num in N:
    res += int(num)
print(res)
```

