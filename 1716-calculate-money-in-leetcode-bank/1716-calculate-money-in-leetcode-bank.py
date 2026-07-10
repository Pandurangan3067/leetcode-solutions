class Solution:
    def totalMoney(self, n: int) -> int:
        s,j=0,0
        i,k=1,1
        while i<=n:
            s=s+j+k

            if i%7==0:
                k=0
                j+=1
            i+=1
            k+=1

        return s