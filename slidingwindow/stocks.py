class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        maxval = 0

        while j < len(prices):
            price = prices[j] - prices[i]
            maxval = max(maxval, price)
            if price < 0:
                i += 1
            else:
                j += 1

        return maxval


sol = Solution()
print(sol.maxProfit([10,1,5,6,7,1]))
