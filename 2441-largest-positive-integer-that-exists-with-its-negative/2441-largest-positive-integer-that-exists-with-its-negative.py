class Solution:
    def findMaxK(self, a: List[int]) -> int:
        m=0
        for i in range(len(a)):   
            m=max(a)
            if m>0 and m*-1 in a:
                return m
            else:
                a[a.index(m)]=0
        return -1