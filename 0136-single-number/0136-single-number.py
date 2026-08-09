class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        l=len(nums)
        if len(nums)==1:
            return nums[0]
        if nums[0]^nums[1]!=0:
            return nums[0]
        for i in range(0,len(nums)-1,2):
            if nums[i]^nums[i+1] !=0:
                return nums[i]
        if nums[l-2]^nums[l-1]!=0:
            return nums[l-1]
                