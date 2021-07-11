"""
Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward. For example, 121 is palindrome while 123 is not.
"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        x_str = str(x)

        return x_str == x_str[::-1]
