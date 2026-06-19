class Solution:
    def addToArrayForm(self, a: List[int], k: int) -> List[int]:
        n=len(a)
        r,i=0,-1
        d=0
        while k>0 and n>0:
            q=a[i]+k%10+r
            r=q//10
            a[i]=q%10 
            i-=1
            k//=10
            n-=1
            print(a)
        if k==0:
            while n>0:
                q=a[i]+r
                r=q//10
                a[i]=q%10 
                i-=1
                n-=1
                print(a)
        else:
            while k>0:
                q=k%10+r
                r=q//10
                a.insert(0,q%10)
                k//=10
                print(a)
    
        if r>0:
            a.insert(0,r)
            print(a)
        return a
