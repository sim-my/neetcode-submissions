class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)*len(grid)

        flat = [x for row in grid for x in row]
        count = Counter(flat)
        result = [None,None]
        for i in range(1, n+1):
            print(i)
            if count[i] == 2:
                result[0] = i
            if count[i] == 0:
                result[1] = i

            if result[0] and result[1]:
                break

        return result
