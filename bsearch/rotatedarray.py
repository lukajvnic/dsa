class Solution:

	def search(self, nums, left, right):
		print(left, right)
		mid = (left + right) // 2

		if nums[mid] < nums[mid - 1]:
			return nums[mid]

		if nums[mid] > nums[-1]:
			return self.search(nums, mid + 1, right)  # go right
		return self.search(nums, left, mid - 1)  # go left

	def findMin(self, nums: list[int]) -> int:
		if len(nums) == 1:
			return nums[0]
		return self.search(nums, 0, len(nums) - 1)
        
sol = Solution()
print(sol.findMin([3,4,5,6,1,2]))
