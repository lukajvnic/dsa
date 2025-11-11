class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}
        for i, num in enumerate(nums):
            h[target - num] = i
            if num not in h:
                h[num] = None
        
        for j, num in enumerate(nums):
            if h[num] is not None and h[num] != j:
                if j < h[num]:
                    return [j, h[num]]
                return [h[num], j]
        

sol = Solution()
print(sol.twoSum([1,3,4,2], 6))
