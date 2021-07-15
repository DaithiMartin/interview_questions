"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 != 0:
            return False

        open_to_close = {"(": ")",
                         "{": "}",
                         "[": "]"}
        close = (")", "}", "]")
        stack = []
        for char in s:
            if char in open_to_close:
                stack.append(char)
                continue

            if char in close:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if char != open_to_close[top]:
                    return False

        return True if len(stack) == 0 else False
