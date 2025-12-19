#1281. Subtract the Product and Sum of Digits of an Integer

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod=1
        total=0

        while n:
            d=n%10
            prod*=d
            total+=d
            n//=10

        return prod-total
