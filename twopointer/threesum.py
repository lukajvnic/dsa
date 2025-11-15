class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1

        while True:
            s = numbers[j] + numbers[i]

            if s == target:
                return [i, j]

            if s > target:
                j -= 1
            if s < target:
                i += 1
        
        return None

    def threeSum(self, nums: list[int]):
        l = sorted(nums)
        out = []

        for num in l:
            s = self.twoSum(l, -num)
            if s is not None:
                _set = sorted([l[s[0]], l[s[1]], num])
                if _set not in out:
                    out.append(_set)

        return out
        

sol = Solution()
print(sol.threeSum([-1,0,1,2,-1,-4]))
