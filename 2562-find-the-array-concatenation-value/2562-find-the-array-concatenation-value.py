class Solution:
    def findTheArrayConcVal(self, a: List[int]) -> int:
        l,r=0,len(a)-1
        s=0
        while l<r:
            c=str(a[l])+str(a[r])

            s+=int(c)
            l+=1
            r-=1
        if l==r:
            s+=a[l]
        return s