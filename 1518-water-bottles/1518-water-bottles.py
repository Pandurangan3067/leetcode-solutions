class Solution:
    def numWaterBottles(self, a: int, b: int) -> int:
        c=a
        while a//b>0:
            c=c+(a//b)
            a=(a%b)+(a//b)
        return c