class Solution:
    def applyOperations(self, a: List[int]) -> List[int]:
        n=len(a)
        for i in range(n-1):
            if a[i]==a[i+1]:
                a[i]=2*a[i]
                a[i+1]=0
        li=[0]*n
        l,r=0,n-1
        for i in range(n):
            if a[i]==0:
                li[r]=a[i]
                r-=1
            else:
                li[l]=a[i]
                l+=1
        return li