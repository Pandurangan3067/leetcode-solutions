class Solution:
    def mergeAlternately(self, a: str, b: str) -> str:
        i,j=0,0
        s=""
        n,m=len(a),len(b)
        while i<n and j<m:
            s+=a[i]+b[j]
            i+=1
            j+=1
        if i==n:
            s+=b[j:]
        else:
            s+=a[i:]
        return s