class Solution:
    def digitCount(self, num: str) -> bool:
        n=len(num)
        c=0
        for i in range(len(num)):
            if num.count(str(i))!=int(num[i]):
                return False
        return True