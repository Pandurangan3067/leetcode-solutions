class Solution:
    def findFinalValue(self, nums: List[int], o: int) -> int:
        while True:
            if o not in nums:
                return o
            else:
                o*=2
        