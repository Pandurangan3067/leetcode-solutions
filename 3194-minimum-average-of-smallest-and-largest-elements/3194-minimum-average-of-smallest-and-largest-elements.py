class Solution:
    def minimumAverage(self, a: List[int]) -> float:
        a.sort()
        l,r=0,len(a)-1
        li=[]
        while l<=r:
            li.append((a[l]+a[r])/2)
            l+=1
            r-=1
        return min(li)