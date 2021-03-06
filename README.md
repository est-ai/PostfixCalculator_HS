# Postfix Calculator
- 목표 : infix notation(중위표기식)을 postfix 로 변환하여 사칙연산을 계산하는 계산기를 만드는 것

## 1. Input spec
- 사용가능한 연산자는 +, -, *, /, (, ) 총 6가지로 정의한다.
- 사용가능한 피연산자는 정수(int), 소수점(float), 음수(negative number) 를 모두 포함한다.
- 연산자와 피연산자 사이의 공백을 허용한다. 
- 음수를 표현할 때에는 괄호 속에 넣어서 정의한다(가장 첫 피연산자가 음수인 경우는 제외한다)
  - 가장 첫 피연산자가 음수인 경우 : -3 + 5
  - 그 외 음수의 표현: 2 * (-3) / 2 

## 2. Lexeme Analyzer 
- input : 수식 문자열
- output : postfix 배열 

1. 수식 안의 공백을 모두 제거
2. 수식의 글자를 하나씩 반복문으로 처리
   2-1. 피연산자가 나오는 경우
      2-1-1. 현재 문자가 소수점이라면
         - 마지막 postfix 에 소수점 추가
      2-1-2. 마지막 potfix에 소수점이 포함되어 있고, 수식에서 현재 글자 앞의 글자가 숫자나 소수점인 경우
         - 연속된 소수점이라고 판단하여, postfix 마지막 글자에 연결
      2-1-3. stack 의 마지막 값이 '-' 이면서, 뺄셈이 아닌 경우
         - stack에서 '-'을 제거하고, 현재 문자의 음수값을 postfix 에 추가
      2-1-4. 그 외의 모든 피연산자는 postfix 에 추가
   2-2. 여는 괄호가 나오는 경우
      - 여는 괄호를 stack에 추가
   2-3. 닫는 괄호가 나오는 경우
      - stack 에서 여는 괄호가 나올 때 까지 stack에 있는 값을 postfix에 추가
   2-4. 연산자가 나오는 경우 
      - stack이 비어있지 않고, stack의 마지막 값이 여는 괄호가 아니며, stack의 마지막 값의 우선순위가 현재 연산자의 우선순위보다 높다면 반복적으로 postfix에 추가
      - 현재 연산자를 stack에 추가
3. stack 에 연산자가 남아있다면 모두 postfix에 추가

## 3. Calculate postfix
- input : postfix 배열
- output : 계산 결과 값

1. postfix를 하나씩 반복문으로 처리
   1. 현재 글자가 연산자인 경우
      - stack 으로 부터 두 개의 값을 pop 하며, 첫번쨰 값을 b, 두번쨰 값을 a로 선언
        - 왜 순서가 바뀌는거 : pop의 추출 시 순서는 역순으로 되기 때문에
      1. 현재 연산자가 + 인 경우 => a + b
      2. 현재 연산자가 - 인 경우 => a - b
      3. 현재 연산자가 * 인 경우 => a * b
      4. 현재 연산자가 / 인 경우 => a / b 
   2. 현재 글자가 피연산자인 경우
      - float 형태로 변환 후 stack 에 추가

- lexer의 역할
  - valid 한지 판별하는 함수
    - token이 valid한지
- parser
  - 수식이 valid한지

수식이 들어왔을때
    1. 이 수식과 토큰이 valid한가?
    2. 계산?

- CFG와 연산자 우선순위, 모호성(- BNF)
- recursive dependency parser
```python

```