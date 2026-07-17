class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}

        for num in nums:
            dict[num] = 1 + dict.get(num, 0)
        
        result = []

        for num, i in dict.items():
            result.append([i, num])


        result.sort()

        final = []

        for i in range(k):
            final.append(result.pop()[1])

        return final

                