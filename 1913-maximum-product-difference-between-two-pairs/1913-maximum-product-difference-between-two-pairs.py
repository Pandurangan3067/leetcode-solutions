class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
      a = b = float('-inf')
      c = d = float('inf')
      for i in nums:
        if i >= a:
          b, a = a, i
        elif i > b:
          b = i
        if i <= c:
          d, c = c, i
        elif i < d:
          d = i
      return (a * b) - (c * d)
         