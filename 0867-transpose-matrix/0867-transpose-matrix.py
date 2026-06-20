

class Solution:
    def transpose(self, a: List[List[int]]) -> List[List[int]]:
        m, n = len(a), len(a[0])
        
        # 1. Properly initialize the result array with dimensions (n x m)
        res = [[0 for _ in range(m)] for _ in range(n)]
        
        # 2. Fill the transposed values
        for i in range(m):
            for j in range(n):
                res[j][i] = a[i][j]
                
        return res