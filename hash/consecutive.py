class Solution:
    def chase(self, k, h, acc):
        if h[k] not in h:
            return acc + 1
        return self.chase(h[k], h, acc + 1)

    def longestConsecutive(self, nums: list[int]) -> int:
        h = {num : num + 1 for num in nums}

        maxstreak = 0
        for num in nums:
            if num - 1 not in h:
                c = self.chase(num, h, 0)
                if c > maxstreak:
                    maxstreak = c

        return maxstreak


sol = Solution()
print(sol.longestConsecutive([0,3,2,5,4,6,1,1]))
