class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        size = len(nums)
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)