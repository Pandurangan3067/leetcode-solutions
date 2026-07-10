class Solution:
    def squareIsWhite(self, a: str) -> bool:
        s="abcdefgh"
      
        return (1+int(a[1])+s.index(a[0]))%2==1