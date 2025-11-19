class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        encountered = set([])
        
        current = 0

        while True:
            value = nums[current]

            if value in encountered:
                return value
            
            encountered.add(value)
            current = value
