class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones or len(stones) == 0:
            return 0
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while stones and len(stones) > 1:
            print(stones)
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            difference = abs(first) - abs(second)
            heapq.heappush(stones,-difference)

        if len(stones) == 0: return 0 
        else: return -stones[0]

