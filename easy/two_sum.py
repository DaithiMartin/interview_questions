"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        value_map = {}  # maps value : index

        for i, number in enumerate(nums):
            diff = target - number

            if diff in value_map:
                return [i, value_map[diff]]
            else:
                value_map[number] = i

        return None