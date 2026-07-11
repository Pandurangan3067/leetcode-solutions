class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        p,n=[],[]
        for i in a:
            if i<0:
                n.append(i)
            else:
                p.append(i)
        i=0
        l=[]
        for i in range(len(a)//2):
            l.append(p[i])
            l.append(n[i])
        return l
