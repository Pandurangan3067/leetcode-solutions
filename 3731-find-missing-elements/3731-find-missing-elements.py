class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        missing_nums = []
        nums.sort()
        nums_list_all = {x for x in range(nums[0],nums[-1]+1)}
        missing_nums = list(nums_list_all - (set(nums)))
        missing_nums.sort()
        return missing_nums