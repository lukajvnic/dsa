import math
import heapq

class Point:
    def __init__(self, x, y):
        self.coord = [x, y]
        self.dist = -math.sqrt((x ** 2) + (y ** 2))
    
    def __eq__(self, other):
        return self.dist == other.dist
    
    def __ne__(self, other):
        return self.dist != other.dist
    
    def __lt__(self, other):
        return self.dist < other.dist

    def __gt__(self, other):
        return self.dist > other.dist

    def __le__(self, other):
        return self.dist <= other.dist

    def __ge__(self, other):
        return self.dist >= other.dist


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for coords in points:
            p = Point(*coords)
            print(p.dist, [h.dist for h in heap])
            if len(heap) < k:
                heapq.heappush(heap, p)
            elif abs(p.dist) < abs(heap[0].dist):
                heapq.heappop(heap)
                heapq.heappush(heap, p)            
        
        return [p.coord for p in heap]

