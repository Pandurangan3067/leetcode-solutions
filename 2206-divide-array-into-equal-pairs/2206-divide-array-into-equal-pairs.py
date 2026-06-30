class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        c=0
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        print(d)
        for i in d.values():
            if i%2!=0:
                return False
        return True
                
            