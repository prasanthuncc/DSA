"""
Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.
Example 1:

Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
Constraints:

1 <= tokens.length <= 1000.
tokens[i] is "+", "-", "*", or "/", or a string representing an integer in the range [-100, 100].

"""


def evalRPN(tokens: list[str]) -> int:
    s = []
    for i in tokens:
        if i.strip() not in ('+', '-', '*', '/'):
            s.append(i)
        else:
            a = int(s.pop())
            b = int(s.pop())
            if i == '+':
                result = b + a
            elif i == '-':
                result = b - a
            elif i == '*':
                result = a * b
            else:
                # Here we cant use // coz // will round toward negative infinity for negative values like
                # say we have -7//3 here we expect answer to be -3 (rounded towards zero) but it would be -4 (rounded towards -infinity)
                # similarly say we get int(-0.1234/5) will give zero
                result = int(b / a)
            s.append(str(result))
    return int(s.pop())


if __name__ == '__main__':
    print(evalRPN(tokens=["1", "2", "+", "3", "*", "4", "-"]))
    print(evalRPN(tokens=["4", "13", "5", " / ", " + "]))
    print(evalRPN(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
