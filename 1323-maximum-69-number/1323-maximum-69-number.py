class Solution:
    def maximum69Number (self, num: int) -> int:
        s=str(num)
        v,n=0,len(s)
        for i in range(n):
            if s[i]=="6":
                v=(v*10)+9

                break
            else:
                v=(v*10)+int(s[i])
          
        while i+1<n:
            v=(v*10)+int(s[i+1])
            i+=1
            
        return v