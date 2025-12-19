#1464. Maximum Product of Two Elements in an Array

class Solution:
    def maxProduct(self, nums):
        a,b = sorted(nums)[-2:]
        return(a-1)*(b-1)
        
