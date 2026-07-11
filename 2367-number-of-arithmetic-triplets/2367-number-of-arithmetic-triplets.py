class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        nums_set = set(nums)
        count = 0
        for num in nums:
            if (num + diff in nums_set) and (num + 2 * diff in nums_set):
                count += 1
        return count