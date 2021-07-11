"""
Given a string s, find the length of the longest substring without repeating characters.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        char_index = {}
        start_ptr = 0
        max_len = 0
        for i, char in enumerate(s):
            # second bool check ensures we only move the pointer forward
            if char in char_index and start_ptr <= char_index[char]:
                start_ptr = char_index[char] + 1
            else:
                max_len = max(max_len, i - start_ptr + 1)
            char_index[char] = i

        return max_len