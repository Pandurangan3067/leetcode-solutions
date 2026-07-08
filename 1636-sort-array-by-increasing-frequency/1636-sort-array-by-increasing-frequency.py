class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        d={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        s=d.items()
        s = sorted(s, key=lambda x: (x[1], -x[0]))
        l=[]
        for i in s:
            l+=[i[0]]*i[1]
        return l