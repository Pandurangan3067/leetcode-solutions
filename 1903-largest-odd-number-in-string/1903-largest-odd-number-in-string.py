class Solution:
    def largestOddNumber(self, a: str) -> str:
        i=len(a)-1
        while i>-1:
            if int(a[i])%2==1:
                return a[:i+1]
            i-=1
        return ""