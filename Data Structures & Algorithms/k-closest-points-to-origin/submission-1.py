class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            dist = y*y + x*x
            heapq.heappush(heap, (dist, [x,y]))

        return [point for _, point in heapq.nsmallest(k, heap)]