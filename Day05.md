# Python



## 제어문

- 파이썬은 기본적으로 위에서부터 아래로 차례대로 명령을 수행
- 특정 상황에 따라 코드를 선택적으로 실행(분기/조건) 하거나 계속하여 실행(반복)하는 제어가 필요함
- 제어문은 순서도(flowchart)로 표현이 가능



## 조건문

- 조건문은 참/거짓을 판단할 수 있는 조건식과 함께 사용

- 기본 형식

  - 조건에는 참/거짓에 대한 조건식

  - 조건이 참인 경우 이후 들여쓰기 되어있는 코드 블록을 실행

  - 이외의 경우 else이후 들여쓰기 되어있는 코드 블록을 실행

    - else는 선택적으로 활용할 수 있음

      ```python
      if 조건:
          # Code block
      else:
          # Code block
      ```

- 복수 조건문

  - 복수의 조건식을 활용할 경우 elid를 활용하여 표현함

    ```python
    if 조건:
    	# Code block
    elif 조건:
    	# Code block
    elif 조건:
    	# Code block
    else:
    	# Code block
    ```

- 중첩 조건문

  - 조건문은 다른 조건문에 중첩되어 사용될 수 있음

    - 들여쓰기에 유의하여 작성할 것

    ```python
    if 조건:
        # Code block
        if 조건:
            # Code block
    else:
        # Code block 
    ```



## 조건 표현식

- 조건 표현식(Conditional Expression)이란?

  - 조건 표현식을 일반적으로 조건에 따라 값을 정할 때 활용

  - 삼항 연산자(Ternary Operator)로 부르기도 함

    ```python
    true인 경우 값 if 조건 else false인 경우 값
    ```

  - 절댓값을 저장하기 위한 코드

    ```python
    value = num if num >= 0 else -num
         # 참일경우             # 거짓일 경우
    ```

  - 조건 표현식으로 변환

    ```python
    num = 2
    if num % 2:
        result = '홀수입니다.'
    else:
        result = '짝수입니다.'
    print(result)
    
    # 짝수입니다.
    ```

    ```python
    num = 2
    result = '홀수입니다.' if num % 2 else '짝수입니다.'
    print(result)
    
    # 짝수입니다.
    ```



## 반복문

- 특정 조건을 만족할 때까지 같은 동작을 계속 반복하고 싶을 때 사용
- 반복문의 종류
  - while 문
    - 종료 조건에 해당하는 코드를 통해 반복문을 종료시켜야 함
  - for 문
    - 반복가능한 객체를 모두 순회하면 종료 (별도의 종료 조건이 필요 없음)
  - 반복 제어
    - break, continue, for-else



## while 문

- while문은 조건식이 참인 경우 반복적으로 코드를 실행

  - 조건이 참인 경우 들여쓰기 되어 있는 코드 블록이 실행됨

  - 코드 블록이 모두 실행되고, 다시 조건식을 검사하며 반복적으로 실행됨

  - while문은 무한 루프를 하지 않도록 종료 조건이 반드시 필요

    ```python
    while 조건:
        # Code block
    ```

- 복합 연산자(In-Place Operator)

  - 복합 연산자는 연산과 할당을 합쳐 놓은 것
    - 예시) 반복문을 통해서 개수를 카운트 하는 경우



## for문

- for문은 시퀀스(string, tuple, list, range)를 포함한 순회 가능한 객체(iterable)의 요소를 모두 순회

  - 처음부터 끝까지 모두 순회하므로 별도의 종료 조건이 필요하지 않음

- Iterable

  - 순회할 수 있는 자료형(string, list, dict, tuple, range, set 등)

  - 순회형 함수(range, enumerate)

    ```python
    for 변수명 in iterable:
        # Code block
    ```

- for문을 이용한 문자열(String)순회

  - 문자열이 한 글자씩 출력된다.

- 딕셔너리(Dictionary) 순회

  - 딕셔너리는 기본적으로 key를 순회하며, key를 통해 값을 활용

- 추가 메서드를 활용한 딕셔너리(Dictionary) 순회

  - key() : key로 구성된 결과
  - values() : value로 구성된 결과
  - items() : (key, value)의 튜플로 구성된 결과

- enumerate 순회

  - enumerate()

    - 인덱스와 객체를 쌍으로 담은 열거형(enumerate) 객체 반환
      - (index, value)형태의 tuple로 구성된 열거 객체를 반환

    ```python
    members = ['민수', '영희', '철수']
    enumerate(members) 
    print(list(enumerate(members))). # [(0, '민수'), (1, '영희'), (2, '철수')]
    print(list(enumerate(members, start=1)))  # [(1, '민수'), (2, '영희'), (3, '철수')]
    ```

- List Comprehension

  - 리스트 표현식

  - 표현식과 제어문을 통해 특정한 값을 가진 리스트를 간결하게 생성하는 방법

    ```python
    [code for 변수 in iterable]
    
    [code for 변수 in iterable if 조건식]
    ```

  ```python
  a = []
  
  for i in range(5):
      if a.append(i)
  
  a = [i for i in range(5)]
  ```

  

  - 1~3의 세제곱의 결과가 담긴 리스트를 만드시오

    ```python
    # for 문
    cubic_list = []
    for number in range(1, 4):
        cubic_list.append(number ** 3)
    print(cubic_list)  # [1, 8, 27]
    
    # 리스트 표현식
    cubic_list = [number ** 3 for number in range(1, 4)]
    print(cubic_list)  # [1, 8, 27]
    ```

    

  - 1~3의 세제곱의 결과가 담긴 딕셔너리를 만드시오

    ```python
    # for 문
    cubic_dict = {}
    for number in range(1, 4):
        cubic_dict[number] = number ** 3
    print(cubic_dict)  # {1: 1, 2: 8, 3:27}
    
    # 딕셔너리 표현식
    cubic_dict = {number: number ** 3 for number in range(1, 4)}
    print(cubic_dict)  # {1: 1, 2: 8, 3:27}
    ```

    

    

## 반복문 제어

- 반복문 제어
  - break
    - 반복문을 종료
  - continue
    - continue 이후의 코드 블록은 수행하지 않고, 다음 반복을 수행
  - for-else
    - 끝까지 반복문을 실행한 이후에 else 문 실행
      - break를 통해 중간에 종료되는 경우 else 문은 실행되지 않음
  - pass
    - 아무것도 하지 않음(문법적으로 필요하지만, 할 일이 없을 때 사용)