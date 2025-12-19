#1512. Number of Good Pairs

class Solution:
    def numIdenticalPairs(self, nums):
        freq = {}
        res = 0

        for n in nums:
            res += freq.get(n, 0)
            freq[n] = freq.get(n, 0) + 1

        return res
        
