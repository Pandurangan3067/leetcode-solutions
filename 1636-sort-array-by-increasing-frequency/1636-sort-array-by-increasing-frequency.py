class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mp={}
        for i in range(len(nums)):
            if nums[i] in mp:
                mp[nums[i]]+=1
            else:
                mp[nums[i]]=1
        nums.sort(key=lambda x:(mp[x],-x))
        return nums