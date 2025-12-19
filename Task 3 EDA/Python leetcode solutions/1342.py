#1342. Number of Steps to Reduce a Number to Zero

class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0
        while num:
            steps += 1
            num = num >> 1 if num % 2 == 0 else num - 1
        return steps
        
