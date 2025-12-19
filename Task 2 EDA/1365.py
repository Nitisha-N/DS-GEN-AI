#1365. How Many Numbers Are Smaller Than the Current Number

from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)
        pos = {}

        for i, v in enumerate(sorted_nums):
            if v not in pos:
                pos[v] = i

        return [pos[n] for n in nums]
