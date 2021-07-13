"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = strs[0]

        for s in strs:
            # null case
            if len(s) == 0:
                return ""

            # make prefix and string same length
            if len(s) > len(prefix):
                s = s[: len(prefix)]
            elif len(prefix) > len(s):
                prefix = prefix[: len(s)]

            # iterate through string and shorten prefix when matching stops
            for i, char in enumerate(s):
                if char != prefix[i]:
                    prefix = prefix[:i]
                    break

        return prefix
