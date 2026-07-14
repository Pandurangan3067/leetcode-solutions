class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n,m=min(nums),max(nums)
        l=[]
        for i in range(n,m+1):
            if i not in nums:
                l.append(i)
        return l