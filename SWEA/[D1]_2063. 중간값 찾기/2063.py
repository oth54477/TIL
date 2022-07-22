N = int(input())
numbers = list(map(int, input().split()))

numbers.sort()  # 리스트 numbers 오름차순 정렬

middle_index = N // 2  # 숫자 개수N이 홀수일 경우 중간값은 N // 2
middle_number = numbers[middle_index]  # numbers에서 N//2번 값을 middle_number에 저장
print(middle_number)
