# Python

# 함수

## 함수 기초

- 함수를 사용하는 이유
    - Decomposition (분해)
        - 기능을 분해하고
        - 재사용 가능하게 만들고
    - Abstraction (추상화)
        - 복잡한 내용을 모르더라도 사용할 수 있도록
        - 재사용성과 가독성, 생산성
    
- 함수의 종류
    - 내장 함수
        - 파이썬에 기본적으로 포함된 함수
    - 외장 함수
        - import 문을 통해 사용하며, 외부 라이브러리에서 제공하는 함수
    - 사용자 정의 함수
        - 직접 사용자가 만드는 함수
        
- 함수의 정의
    - 함수(Function)
        - 특정한 기능을 하는 코드의 조각(묶음)
        - 특정 코드를 매번 다시 작성하지 않고, 필요시에만 호출하여 사용

- 함수 기본 구조
    - 선언과 호출 (define & call)
    - 입력 (input)
    - 문서화 (Docstring)
    - 범위 (Scope)
    - 결과값 (Output)

- 선언과 호출 (define & call)
    - 함수의 선언은 def 키워드를 활용함
    - 들여쓰기를 통해 Function body(실행될 코드 블록)를 작성함
        - Docstring은 함수 body앞에 선택적으로 작성 가능
            - 작성 시에는 반드시 첫 번째 문장에 분자열 “””
    - 함수는 parameter를 넘겨줄 수 있음
    - 함수는 동작 후에 return을 통해 결괏값을 전달함

- 함수의 정의
    - 함수를 사용하기 위해서는 먼저 함수를 정의해야 함
        
        ```python
        def function_name(parameter):
            # Code block
            return retuning_value
        ```
        

## 함수의 결과값 (Output)

- Void function
    - 명시적인 return 값이 없는 경우, None을 반환하고 종료
- Value returning function
    - 함수 실행 후, return문을 통해 값 반환
    - return을 하게 되면, 값 반환 후 함수가 바로 종료
    - print는 값을 출력하지만, 값을 반환하진 않습니다.
- 주의 : print vs return
    - print 함수화 return의 차이점
        - print를 사용하면 호출될 때마다 값이 출력됨(주로 테스트를 위해 사용)
        - 데이터 처리를 위해서는 return사용
- 두 개 이상의 값 반환해야 하는 경우
    - 반환값으로 튜플 사용
- 함수 반환 정리
    - return이 없을 때 → None
    - return → 하나를 만환
    - 여러 개를 원하면 → Tuple활용 (혹은 리스트와 같은 컨테이너 활용)

## 함수의 입력 (Input)

- Parameter : 함수를 정의할 때, 함수 내부에서 사용되는 변수
- Argument : 함수를 호출 할 때, 넣어주는 값
- Argument란?
    - 함수 호출 시 함수의 parameter를 통해 전달되는 값
    - Argument는 소괄호 안에 할당 func_name(argument)
        - 필수 Argument : 반드시 전달되어야 하는 argument
        - 선택 Argument : 값을 전달하지 않아도 되는 경우는 기본값이 전달
- Positional Arguments
    - 기본적으로 함수 호출 시 Argument는 위치에 따라 함수 내에 전달됨
- Keyword Argument
    - 직접 변수의 이름으로 특정 Argument를 전달할 수 있음
    - Keyword Argument다음에 Positional Argument를 활용할 수 없음
        
        ```python
        def add(x, y):
            return x + y
        
        add(x=2, y=5)
        add(2, y=5)
        add(x=2, 5) -> Error 발생!
        ```
        
- Default Arguments Values
    - 기본값을 지정하여 함수 호출 시 argument 값을 설정하지 않도록 함
        - 정의된 것 보다 더 적은 개수의 argument 들로 호출될 수 있음
- 정해지지 않은 여러 개의 Argument 처리
    - 애스터리스크(Asterisk) 혹은 언패킹 연산자라고 불리는 *덕분
- 가변 인자(*args)
    - 가변인자란?
        - 여러 개의 Positional Argument를 하나의 필수 parameter로 받아서 사용
    - 가변인자는 언제 사용하는가?
        - 몇 개의 Positional Argument를 받을지 모르는 함수를 정의할 때 유용
- 패킹 / 언패킹
    - 가변 인자를 이해하기 위해서는 패킹, 언패킹을 이해해야 함
    - 패킹
        - 여러개의 데이터를 묶어서 변수에 할당하는 것
            
            ```python
            numbers = (1, 2, 3, 4, 5). # 패킹
            print(numbers). # (1, 2, 3, 4, 5)
            ```
            
    - 언패킹
        - 시퀀스 속의 요소들을 여러 개의 변수에 나누어 할당하는 것
            
            ```python
            numbers = (1, 2, 3, 4, 5)
            a, b, c, d, e = numbers. # 언패킹
            print(a, b, c, d, e)  # 1 2 3 4 5
            ```
            
    - 언패킹시 변수의 개수와 할당하고자 하는 요소의 갯수가 동일해야 함
        
        ```python
        numbers = (1, 2, 3, 4, 5). # 패킹
        a, b, c, d, e, f = numbers # 언패킹
        # ValueError: not enough values to unpack (expected 6, got 5)
        ```
        
    - 언패킹시 왼쪽의 변수에 asterisk(*)를 붙이면, 할당하고 남은 요소를 리스트에 담을 수 있음
        
        ```python
        numbers = (1, 2, 3, 4, 5). # 패킹
        
        a, b, *rest = numbers. # 1, 2를 제외한 나머지를 rest에 대입
        
        a, *rest, e = numbers. # 1, 5를 제외한 나머지를 rest에 대입
        print(rest). # [2, 3, 4]
        ```
        
- Asterisk (*)와 가변 인자
    - *는 스퀸스 언패킹 연산자라고도 불리며, 말 그대로 시퀀스를 풀어 헤치는 연산자
        - 주로 튜플이나 리스트를 언패킹하는데 사용
        - *를 활용하여 가변 인자를 만들 수 있음
- 가변 인자 예시
    - packing을 통해 받은 모든 숫자들의 합을 구하는 함수 만들기
        
        ```python
        def sum_all(*numbers):
            result = 0
        for number in numbers:
                result += number
            return result
        
        print(sum_all(1, 2, 3)  # 6
        print(sum_all(1, 2, 3, 4, 5, 6)  # 21
        ```
        
- 가변 키워드 인자 (**kwargs)
    - 몇 개의 키워드 인자를 받을 지 모르는 함수를 정의할 때 유용
    - **kwargs는 딕셔너리로 묶여 처리되며, parameter에 **를 붙여 표현
        
        ```python
        def family(**kwargs):
            for key, value in kwargs.items():
                print(key, ":", value)
        family(father= ' 아부지 ', mother= ' 어무니 ', baby= ' 아기 '
        ```
        

## 함수의 범위 (Scope)

- global 문
    - 현재 코드 블록 전체에 적용되며, 나열된 식별자(이름)이 global variable임을 나타냄
        - global에 나열된 이름은 같은 코드 블록에서 global앞에 등장할 수 없음
        - gloabal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야 함
- nonlocal
    - global을 제외하고 가장 가까운 (둘러싸고 있는)scope의 변수를 연결하도록 함
        - nonlocal에 나열된 이름은 같은 코드 블록에서 nonlocal앞에 등장할 수 없음
            - nonlocal에 나열된 이름은 parameter, for 루프 대상, 클래스/함수 정의 등으로 정의되지 않아야함
            - global과는 달리 이미 존재하는 이름과의 연결만 가능함
- nonlocal, global 비교
    
    ```python
    # 선언된 적 없는 변수의 활용
    def func1():
        global out
        out = 3
    func1()
    print(out). # 3
    
    # 선언된 적 없는 변수의 활용
    def func1():
        def func2():
            nonlocal y
            y = 2
        func2()
        print(y)    
    func1()
    
    # SyntaxError: no binding for nonlocal 'y' found
    ```
    
- 함수의 범위 주의
    - 기본적으로 함수에서 선언된 변수는
    

## 함수 응용

- map
    - map(function, iterable)
    - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과를  map object로 반환
- map 활용사례
    - 알고리즘 문제 풀이시 input 값들을 숫자로 바로 활용하고 싶을 때
        
        ```python
        n, m = map(int, input().split()) # 3, 5를 입력하면
        print(n, m)  # 3, 5
        print(type(n), type(m)). # <class 'int'> <class 'int'>
        ```
        
- filter
    - filter(function, iterable
    - 순회 가능한 데이터구조(iterable)의 모든 요소에 함수(function)적용하고, 그 결과가 True인 것들을 filter object로 반환
- zip
    - zip(*iterables)
    - 복수의 iterable을 모아 튜플을 원소로 하는 zip object를 반환
- lambda 함수
    - lambda[parameter] : 표현식
    - 람다함수
        - 표현식을 계산한 결과값을 반환하는 함수로, 이름이 없는 함수여서 익명함수 라고도 불림
    - 특징
        - return문을 가질 수 없음
        - 간편 조건문 외 조건문이나 반복문을 가질 수 없음
    - 장점
        - 함수를 정의해서 사용하는 것 보다 간결하게 사용 가능
        - def를 사용할 수 없는 곳에서도 사용 가능
            
            ```python
            # 삼각형의 넓이를 구하는 공식 - def
            def triangle_area(b, h):
                return 0.5 * b * h
            print(triangle_area(5, 6))  #15.0
            
            # 삼각형의 넓이를 구하는 공식 - 람다
            triangle_area = lambda b, h : 0.5 * b * h
            print(triangle_area(5, 6)) # 15.0
            ```
            
- 재귀 함수 (recursive function)
    - 자기 자신을 호출하는 함수
    - 무한한 호출을 목표로 하는 것이 아니며, 알고리즘 설계 및 구현에서 유용하게 활용
        - 알고리즘 중 재귀함수로 조식을 표현하기 쉬운 경우가 있음 (예 - 점화식)
        - 변수의 사용이 줄어들며, 코드의 가독성이 높아짐
    - 1개 이상의 base case(종료되는 상황)가 존재하고, 수렴하도록 작성
        ```python
        def factorial(n):
            if n == 0 or n == 1:
                return 1
            else:
                return n * factorial(n-1)
        print(factorial(4))  # 24
        ```
- 재귀 함수 주의 사항
    - 재귀 함수는 base case에 도달한 때까지 함수를 호출함
    - 메모리 스택이 넘치게 되면(stack overflow)프로그램이 동작하지않게 됨