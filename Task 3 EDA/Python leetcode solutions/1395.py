#1395. Count Number of Teams

from typing import List

class Solution:
    def numTeams(self, rating: List[int]) -> int:
        n = len(rating)
        res = 0

        for j in range(1,n-1):
            left_smaller = sum(r < rating[j] for r in rating[:j])
            left_larger = j - left_smaller

            right_larger = sum(r> rating[j] for r in rating[j+1:])
            right_smaller = (n-j-1)- right_larger

            res += left_smaller * right_larger
            res += left_larger * right_smaller

        return res
