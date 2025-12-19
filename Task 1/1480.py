#1480. Running Sum of 1d Array

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        total = 0

        for n in nums:
            total +=n
            res.append(total)

        return res
        
