"""
Given a signed 32-bit integer x, return x with its digits reversed.
If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
"""


class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        rev_int = int(str(abs(x))[::-1]) * sign
        limit = 2 ** 31

        if -limit <= rev_int <= limit - 1:
            return rev_int
        else:
            return 0