# 2063. 중간값 찾기

- List.sort()함수 사용해 오름차순 정렬
  - List.sort(reverse=True)는 내림차순 정렬
- 리스트 길이의 몫을 활용해 중간값 찾기

```python
N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()  # 리스트 numbers 오름차순 정렬

middle_index = N // 2  # 숫자 개수N이 홀수일 경우 중간값은 N // 2
middle_number = numbers[middle_index]  # numbers에서 N//2번 값을 middle_number에 저장
print(middle_number)

```



