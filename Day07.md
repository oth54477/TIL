# Python : 데이터 구조 및 활용

## 파이썬 공식 문서의 표기법

- python 구문이 아니며, 문법을 표현하기 위한 것임
- 아래 예시에서 `str.replace(old, new[, count])
  - old, new는 필수 / [, count]는 선택적 인자를 의미함

## 문자열(String Type)

- .isdecimal() → .isdigit() → .isnumeric()

- 문자열 변경 메서드(S는 문자열)

  | 문법                           | 설명                                                                            |
  | ------------------------------ | ------------------------------------------------------------------------------- |
  | s.replace(old, new[, count])   | 바꿀 대상 글자를 새로운 글자로 바꿔서 반환                                      |
  | s.strip([chars])               | 공백이나 특정 문자를 제거                                                       |
  | s.split(sep=None, maxsplit=-1) | 공백이나 특정 문자를 기준으로 분리                                              |
  | ‘separator’.join([iterable])   | 구분자로 iterable을 합침                                                        |
  | s.capitalize()                 | 가장 첫 번째 글자를 대문자로 변경                                               |
  | s.title()                      | 문자열 내 띄어쓰기 기준으로 각 단어의 첫글자는 대문자로, 나머지는 소문자로 변환 |
  | s.upper()                      | 모두 대문자로 변경                                                              |
  | s.lower()                      | 모두 소문자로 변경                                                              |
  | s.swapcase()                   | 대 < - > 소문자 서로 변경                                                       |

- 문자열은 immutable(불변형)인데, 문자열 변경이 되는 이유?

  - 기존의 문자열을 변경하는 게 아니라, 변경된 문자열을 새롭게 만들어서 반환
    - ex) replace, strip, title

- 문자열 변경

  - .replace(old, new[, count])

    - 바꿀 대상 글자를 새로운 글자로 바꿔서 반환
    - count를 지정하면, 해당 개수만큼만 시행

  - .strip([chars])

    - 특정한 문자들을 지정하면,
      - 양쪽을 제거하거나(strip), 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip)
    - 문자열을 지정하지 않으면 공백을 제거함

  - .split(sep=None, maxsplit=-1)

    - 문자열을 특정한 단위로 나눠 리스트로 반환
      - sep이 None이거나 지정되지 않으면 연속된 공백문자를 단일한 공백문자로 간주하고,  선행/후행 공백은 빈 문자열에 포함시키지 않음.
      - maxsplit이 -1인 경우에는 제한이 없음

  - ‘separator’.join([iterable])

    - 반복가능한(iterable)컨테이너 요소들을 separator(구분자)로 합쳐 문자열 반환

      - iterable에 문자열이 아닌 값이 있으면 TypeError 발생

        ```python
        print('!'.join('ssafy')) # 's!s!a!f!y'
        print(' '.join(['3', '5'])) # '3 5'
        ```

        ```python
        # 문자열 변경 예시
        
        msg = 'hI! Everyone, I\\'m ssafy'
        
        print(msg) # 'hI! Everyone, I\\'m ssafy'
        print(msg.capitalize()) # 'Hi! everyone, i\\'m ssafy'
        print(msg.title()) # 'Hi! Everyone, I\\'M Ssafy'
        print(msg.upper()) # 'HI! EVERYONE, I\\'M SSAFY'
        print(msg.lower()) # 'hi! everyone, i\\'m ssafy'
        print(msg.swapcase()) # 'Hi! eVERYONE, i\\'M SSAFY'
        ```

    ## 리스트

    - 리스트는 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용

    - 리스트의 생성과 접근

      - 리스트는 대괄호([]) 혹은 list()를 통해 생성
        - 파이썬에서는 어떠한 자료형도 저장할 수 있으며, 리스트 안에 리스트도 넣을 수 있음
        - 생성된 이후 내용 변경이 가능 → 가변 자료형
        - 이러한 유연성 때문에 파이썬에서 가장 흔히 사용
      - 순서가 있는 시퀀스로 인덱스를 통해 접근 가능
        - 값에 대한 접근은 list[i]

      | 문법                                  | 설명                                                          |
      | ------------------------------------- | ------------------------------------------------------------- |
      | L.append(x)                           | 리스트 마지막에 항목 x를 추가                                 |
      | L.insert(i, x)                        | 리스트 인덱스 i에 항목 x를 삽입                               |
      | L.remove(x)                           | 리스트 가장 왼쪽에 있는 항목(첫 번째) x를 제거                |
      | 항목이 존재하지 않을 경우, ValueError |                                                               |
      | L.pop()                               | 리스트 가장 오른쪽에 있는 항목(마지막)을 반한 후 제거         |
      | L.pop(i)                              | 리스트의 인덱스 i에 있는 항목을 반환 후 제거                  |
      | L.extend(m)                           | 순회형 m의 모든 항목들의 리스트 끝에 추가( +=과 같은 기능)    |
      | L.index(x, start, end)                | 리스트에 있는 항목 중 가장 왼쪽에 있는 항목 x의 인덱스를 반환 |
      | L.reverse()                           | 리스트를 거꾸로 정렬                                          |
      | L.sort()                              | 리스트를 정렬 (매개변수 이용 가능)                            |
      | L.count(x)                            | 리스트에서 항목 x가 몇 개 존재하는지 개수를 반환              |

    - 값 추가 및 삭제

      - .append(x)

        - 리스트에 값을 추가함 (마지막)

      - .insert(i,x)

        - 정해진 위치 i에 x값을 추가함

      - .extend(iterable)

        - 리스트에 iterable의 항목을 추가함

        ```python
        cafe = ['starbucks', 'tomntoms', 'hollys']
        cafe.extend(['coffee'])
        print(cafe) # ['starbucks', 'tomntoms', 'hollys', 'coffee']
        
        cafe = ['starbucks', 'tomntoms', 'hollys']
        cafe += ['coffee']
        print(cafe) # ['starbucks', 'tomntoms', 'hollys', 'coffee']
        
        cafe = ['starbucks', 'tomntoms', 'hollys']
        cafe.extend('cup')
        print(cafe) # cafe = ['starbucks', 'tomntoms', 'hollys', 'c', 'u', 'p']
        ```

      - .remove(x)

        - 리스트에서 값이 x인 것 삭제

      - .pop(i)

        - 정해진 위치 i에 있는 값을 삭제하고, 그 항목을 반환함
        - i가 지정되지 않으면, 마지막 항목을 삭제하고 반환함
        - 

      - .clear()

        - 모든 항목을 삭제함

      - .Index(x)

        - x값을 찾아 해당 index 값을 반환

      - .count(x)

        - 원하는 값의 개수를 반환함

      - .sort()

        - 원본 리스트를 정렬함. None 반환

        - sorted 함수와 비교할 것

          ```python
          numbers = [3, 2, 5, 1]
          result = numbers.sort()
          print(numbers, result) # [1, 2, 3, 5] None
          
          numbers = [3, 2, 5, 1]
          result = sorted(numbers)
          print(numbers, result) # [3, 2, 5, 1] [1, 2, 3, 5]
          ```

      - .reverse()

        - 순서를 반대로 뒤집음(정렬하는 것이 아님)

    ## 튜플(Tuple)

    - 튜플의 정의
      - 튜플은 여러 개의 값을 순서가 있는 구조로 저장하고 싶을 때 사용
        - 리스트와의 차이점은 생성 후, 담고 있는 값 변경이 불가 (불변 자료형)
      - 항상 소괄호 형태로 사용
    - 튜플 관련 메서드
      - 튜플은 변경할 수 없기 때문에 값에 영향을 미치지 않는 메서드 만을 지원
      - 리스트 메서드 중 항목을 변경하는 메서드들을 제외하고 대부분 동일

    ## 연산자(Operator)

    - 멤버십 연산자(Membership Operator)
      - 멤버십 연산자 in을 통해 특정 요소가 속해 있는지 여부를 확인
    - 시퀀스형 연산자(Sequence Type Operator)
      - 산술연산자(+)
        - 시퀀스 간의 concatenation(연결/연쇄)
      - 반복연산자(*)
        - 시퀀스를 반복

    ## 셋(Set)

    - 셋(Set)

      - Set이란 중복되는 요소가 없이, 순서에 상관없는 데이터들의 묶음

        - 데이터의 중복을 허용하지 않기 때문에 중복되는 원소가 있다면 하나만 저장
        - 순서가 없기 때문에 인덱스를 이용한 접근 불가능

      - 수학에서의 집합을 표현한 컨테이너

        - 집합 연산이 가능 (여집합을 표현하는 연산자는 별도로 존재 X)
        - 중복된 값이 존재하지 않음

      - 담고 있는 요소를 삽입 변경, 삭제 가능 → 가변 자료형 (mutable)

        | 문법                                | 설명                                                                          |
        | ----------------------------------- | ----------------------------------------------------------------------------- |
        | s.copy()                            | 셋의 얕은 복사본을 반환                                                       |
        | s.add(x)                            | 항목 x가 셋 s에 없다면 추가                                                   |
        | s.pop()                             | 셋 s에서 핸덤하게 항목을 반환하고 해당 항목을 제거                            |
        | set이 비어 있을 경우, KeyError      |                                                                               |
        | s.remove(s)                         | 항목 x를 셋 s에서 삭제                                                        |
        | 항목이 존재하지 않을 경우, KeyError |                                                                               |
        | s.discard(x)                        | 항목 x가 셋 s에 있는 경우, 항목 x를 셋 s에서 삭제                             |
        | s.update(t)                         | 셋 t에 있는 모든 항목 중 셋 s에 없는 항목을 추가                              |
        | s.clear()                           | 모든 항목을 제거                                                              |
        | s.isdisjoint(t)                     | 셋 s가 셋t의 서로 같은 항목을 하나라도 갖고 있지 않는 경우, True반환 (서로소) |
        | s.issubset(t)                       | 셋 s가 셋 t의 하위 셋인 경우, True반환                                        |
        | s.issuperset(t)                     | 셋 s가 셋 t의 상위 셋인 경우, True반환                                        |

      얕은 (쌍둥이) vs 깊은 (분신술)

    - 추가 및 변경

      - .add(elem)
        - 셋에 값을 추가
      - .update(*others)
        - 여러 값을 추가

    - 요소 삭제

      - .remove(elem)
        - SET에서 삭제하고, 없으면 KeyError
      - .discard(elem)
        - 셋에서 삭제하고 없어도 에러가 발생하지 않음
      - .pop()
        - 임의의 원소를 제거해 반환
      - .clear
        - 모든 항목을 제거

    - 집합 관련 함수

      - s.isdisjoint(t)
        - 셋 s가 셋t의 서로 같은 항목을 하나라도 갖고 있지 않는 경우, True반환 (서로소)
      - s.issubset(t)
        - 셋 s가 셋 t의 하위 셋인 경우, True반환
      - s.issuperset(t)
        - 셋 s가 셋 t의 상위 셋인 경우, True반환

    ## 딕셔너리 (Dictionary)

    - 딕셔너리의 정의
      - 키-값(key-value)쌍으로 이뤄진 자료형(3.7부터는 ordered, 이하 버전은 unordered)
      - Dictionary의 키(key)
        - key는 변경 불가능한 데이터(immutable)만 활용 가능
          - string, integer, float, boolean, tuple, range
      - 각 키의 값(values)
        - 어떠한 형태든 관계없음

    ## 얕은 복사와 깊은 복사 (Shallow Copy & Deep Copy)

    - 할당 (assignment)

      - 대입 연산자 (=)
        - 리스트 복사 확인하기

      ```python
      original_list = [1, 2, 3]
      copy+list = original_list
      print(original_list, copy_list) # [1, 2, 3] [1, 2, 3]
      
      copy_list[0] = 'hello'
      print(original_list, copy_list) # ['hello', 2, 3] ['hello', 2, 3]
      
      ## 대입 연산자를 통한 복사는 해당 객체에 대한 객체 참조를 복사 ##
      ```

    - 얕은 복사 (Shallow Copy)

      - Slice 연산자 활용하여 같은 원소를 가진 리스트지만 연산된 결과를 복사 (다른 주소)

      ```python
      a = [1, 2, 3]
      b = a[:]
      print(a, b) # [1, 2, 3] [1, 2, 3]
      b[0] = 5
      print(a, b) # [1, 2, 3] [5, 2, 3]
      ```

    - 얕은 복사 (Shallow Copy) 주의사항

      - 복사하는 리스트의 원소가 주소를 참조하는 경우

      ```python
      a = [1, 2, ['a', 'b']]
      b = a[:]
      print(a, b) # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
      b[2][0] = 0
      print(a, b) # [1, 2, [0, 'b']] [1, 2, [0, 'b']]
      ```

    - 깊은 복사 (deep copy)

      - 리스트 복사 확인하기

      ```python
      import copy
      a = [1, 2, ['a', 'b']]
      b = copy.deepcopy(a)
      print(a, b) # [1, 2, ['a', 'b']] [1, 2, ['a', 'b']]
      b[2][0] = 0
      print(a, b) # [1, 2, ['a', 'b']] [1, 2, [0, 'b']]
      ```