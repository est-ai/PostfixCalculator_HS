from unittest import TestCase

from main import PostfixCalculator, LexemeAnalyzer


class CalculateTest(TestCase):
    def __init__(self, *args, **kwargs):
        super(CalculateTest, self).__init__(*args, **kwargs)
        self.calculator = PostfixCalculator()
        self.analyzer = LexemeAnalyzer()

    def test_plus(self):
        equation = "1+1"
        postfix = self.analyzer.lex(equation)
        result = self.calculator.calculate(equation)
        self.assertEqual(" ".join(postfix), "1 1 +")
        self.assertEqual(result, 1 + 1)

    def test_minus(self):
        equation = "1-1"
        postfix = self.analyzer.lex(equation)
        result = self.calculator.calculate(equation)
        self.assertEqual(" ".join(postfix), "1 1 -")
        self.assertEqual(result, 1 - 1)

    def test_multiple(self):
        equation = "1*2"
        postfix = self.analyzer.lex(equation)
        result = self.calculator.calculate(equation)
        self.assertEqual(" ".join(postfix), "1 2 *")
        self.assertEqual(result, 1 * 2)

    def test_divide(self):
        equation = "1/2"
        postfix = self.analyzer.lex(equation)
        result = self.calculator.calculate(equation)
        self.assertEqual(" ".join(postfix), "1 2 /")
        self.assertEqual(result, 1 / 2)

    def test_bracket(self):
        equation = "(1+2)*2/4"
        postfix = self.analyzer.lex(equation)
        result = self.calculator.calculate(equation)
        self.assertEqual(" ".join(postfix), "1 2 + 2 * 4 /")
        self.assertEqual(result, (1 + 2) * 2 / 4)

    def test_decimal_point(self):
        equation = "(3+5) * 2.1*(1.1234-3)/2.2234"
        postfix = self.analyzer.lex(equation)
        result = self.calculator.calculate(equation)
        self.assertEqual(" ".join(postfix), "3 5 + 2.1 * 1.1234 3 - * 2.2234 /")
        self.assertEqual(result, (3+5) * 2.1 * (1.1234 - 3) / 2.2234)

    def test_negative_number(self):
        equation = "(-3+5)*2*(-1)/1"
        postfix = self.analyzer.lex(equation)
        result = self.calculator.calculate(equation)
        self.assertEqual(" ".join(postfix), "-3 5 + 2 * -1 * 1 /")
        self.assertEqual(result, (-3 + 5) * 2 * (-1) / 1)

    def test_multiple_bracket(self):
        equation = "(((-2 + 5) * 2 + 1) /2 -1 * (5 -3)) + 2"
        postfix = self.analyzer.lex(equation)
        result = self.calculator.calculate(equation)
        self.assertEqual(" ".join(postfix), "-2 5 + 2 * 1 + 2 / 1 5 3 - * - 2 +")
        self.assertEqual(result, (((-2 + 5) * 2 + 1) / 2 - 1 * (5 - 3)) + 2)

    def test_valid_syntax(self):
        equation = "(1 + 2"
        self.assertRaises(SyntaxError, lambda: self.calculator.calculate(equation))

        equation = "1 + "
        self.assertRaises(SyntaxError, lambda: self.calculator.calculate(equation))

        equation = "1  2"
        self.assertRaises(SyntaxError, lambda: self.calculator.calculate(equation))
