import heapq


class KthLargest:
	def __init__(self, k, nums):
		self.k = k
		self.heap = []
		for num in nums:
			self.add(num)

	def add(self, num):
		if len(self.heap) < self.k:
			heapq.heappush(self.heap, num)
		elif num >= self.heap[0]:
			heapq.heappushpop(self.heap, num)
		return self.heap[0]