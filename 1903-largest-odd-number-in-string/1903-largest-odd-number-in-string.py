class Solution:
    def largestOddNumber(self, num: str) -> str:
        n=len(num)-1
        for i in range(n,-1,-1):
            if num[i] not in "13579":
                continue
            return num[:i+1]
        return ""