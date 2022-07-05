from typing import List


class LexemeAnalyzer:
    def __init__(self):
        self.operator = ("+", "-", "*", "/", "(", ")")
        self.priority = {"+": 1, "-": 1, "*": 2, "/": 2}

    def lex(self, expression: str) -> List[str]:
        """
        infix equation 을 postfix 로 변경하는 함수
        Args:
            expression(str): input equation

        Returns:
            List[str]: postfix

        """
        expression = expression.replace(" ", "")  # 공백 제거
        stack = []
        postfix = []
        for idx, char in enumerate(expression):
            if char not in self.operator:       # 숫자 및 소수점인 경우 postfix에 추가
                if char == ".":
                    postfix[-1] += "."

                elif postfix and "." in postfix[-1] \
                        and (expression[idx-1].isdigit() or expression[idx-1] == "."):  # 소수점
                    # Todo: 1.2.3
                    postfix[-1] += char

                elif stack and "-" == stack[-1] and not expression[idx-2].isdigit():    # 뺄셈 아닌 음수
                    stack = stack[:-1]
                    postfix.append("-" + char)

                else:
                    postfix.append(char)

            elif char == "(":       # 여는 괄호가 나오면 stack에 추가
                stack.append('(')

            elif char == ")":       # 닫는 괄호가 나오면 여는 괄호가 나올때까지 stack에 있는 내용을 postfix에 추가
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()

            else:   # 연산자가 나올 경우
                while stack and stack[-1] != '(' and self.priority[char] <= self.priority[stack[-1]]:
                    postfix.append(stack.pop())
                stack.append(char)

        while stack:    # 스택에 남은 연산자 postfix에 모두 추가
            postfix.append(stack.pop())

        return postfix


class PostfixCalculator:
    """postfix 기반 Calculator"""
    def __init__(self):
        self.lexeme_analyzer = LexemeAnalyzer()
        self.operator = ("+", "-", "*", "/", "(", ")")

    def _validate_equation(self, equation: str) -> bool:
        try:
            eval(equation)

        except (SyntaxError, NameError, ZeroDivisionError):
            return False

        return True

    def calculate(self, equation: str) -> float:
        """
        input equation 이 들어왔을 때 계산하는 함수
        Args:
            equation(str): infix equation

        Returns:
            float: calculation result value

        Raises:
            SyntaxError : 수식이 유효하지 않을 때

        """
        if not self._validate_equation(equation):  # 수식 유효성 검정
            raise SyntaxError("This equation is not valid.")

        postfix = self.lexeme_analyzer.lex(equation)
        return self.calculate_postfix(postfix)

    def calculate_postfix(self, postfix: List[str]) -> float:
        """
        postfix 배열을 받아 계산하는 함수
        Args:
            postfix(List[str]): postfix로 표현된 equation

        Returns:
            float: calculation result value

        """
        stack = []
        for char in postfix:
            if char in self.operator:
                b = stack.pop()
                a = stack.pop()
                if char == "+":
                    stack.append(a + b)

                elif char == "-":
                    stack.append(a - b)

                elif char == "*":
                    stack.append(a * b)

                elif char == "/":
                    stack.append(a / b)
            else:
                stack.append(float(char))

        return float(stack[0])


if __name__ == '__main__':
    calculator = PostfixCalculator()
    analyzer = LexemeAnalyzer()
    input_txt = "1.1.1 + 2"
    print(f"equation : {input_txt}")
    print(f"postfix : {analyzer.lex(input_txt)}")
    print(f"result : {calculator.calculate(input_txt)}")
