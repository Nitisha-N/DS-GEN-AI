#1431. Kids With the Greatest Number of Candies

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        result = []

        for candy in candies:
            can_have_max = candy + extraCandies >= max_candies
            result.append(can_have_max)

        return result
