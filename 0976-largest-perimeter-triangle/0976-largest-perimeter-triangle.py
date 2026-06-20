class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        i,n=2,len(nums)
        m=0
        while i<n:
            if nums[i-2]+nums[i-1]>nums[i] and nums[i-1]+nums[i]>nums[i-2] and nums[i-2]+nums[i]>nums[i-1]:
                if  nums[i-2]+nums[i-1]+nums[i]>m:
                    m=nums[i]+nums[i-1]+nums[i-2]
            i+=1
        return m