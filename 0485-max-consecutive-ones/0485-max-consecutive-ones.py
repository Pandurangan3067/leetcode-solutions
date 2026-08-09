class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m,c=0,0
        for i in nums:
            if i==1:
                c+=1
            else:
                if m<c:
                    m=c
                c=0

        if m<c:
            m=c
        return m
                    
        