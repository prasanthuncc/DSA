"""
Valid Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.
The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.

Example 1:

Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"

Output: true
Example 3:

Input: s = "[(])"

Output: false
Explanation: The brackets are not closed in the correct order.

Constraints:

1 <= s.length <= 1000
"""


def isValid(s: str) -> bool:
    match = {'}': '{', ')': '(', ']': '['}
    stack = []
    for i in s:
        if i in ('{', '[', '('):
            stack.append(i)
        elif i in (']', '}', ')'):
            if not stack or stack.pop() != match.get(i):
                return False
        else:
            continue
    if stack:
        return False
    else:
        return True


if __name__ == '__main__':
    print(isValid(s="[]"))
    print(isValid(s="([{}])"))
    print(isValid(s="[(])"))
    print(isValid(s="]"))
