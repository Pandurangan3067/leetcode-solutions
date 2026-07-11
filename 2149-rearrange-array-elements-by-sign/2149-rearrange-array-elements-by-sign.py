class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        neg = []
        pos = []
        for n in nums:
            if(n<0):
                neg.append(n)
            else:
                pos.append(n)
        res = [0]*(len(nums))
        res[0::2] = pos
        res[1::2] = neg
        return res