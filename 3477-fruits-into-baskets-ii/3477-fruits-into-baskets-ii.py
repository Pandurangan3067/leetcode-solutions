class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        result = len(fruits)
        for fruit in fruits:
            for basket in baskets:
                if basket >= fruit:
                    result -= 1
                    baskets.remove(basket)
                    break

        return result