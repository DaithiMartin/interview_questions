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