class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        
        i = 0
        j = len(numbers) - 1

        while True:
            s = numbers[j] + numbers[i]
            # print(i,j,s)

            if s == target:
                return [i + 1, j + 1]

            if s > target:
                j -= 1
            if s < target:
                i += 1

sol = Solution()
print(sol.twoSum([1,2,3,4],3))
