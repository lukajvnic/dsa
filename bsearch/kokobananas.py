import math

class Solution:

    def simulate(self, piles, h, k):
        total = 0
        for pile in piles:
            total += math.ceil(pile/k)
            if total > h:
                return False
        return True

    # find first index that is true
    def search(self, piles, h, lower, upper):
        k = (upper + lower) // 2
        s = self.simulate(piles, h, k)

        if k == upper:
            return k

        if s:
            if k == lower:
                return k
            return self.search(piles, h, lower, k)  # search lower half
        
        if k == upper:
            return -1  # should never occur due to constraints

        return self.search(piles, h, k + 1, upper)  # search upper half


    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        max_k = max(piles)
        min_k = 1
        return self.search(piles, h, min_k, max_k)


sol = Solution()
piles = [25,10,23,4]
h = 4
print(sol.minEatingSpeed(piles, h))