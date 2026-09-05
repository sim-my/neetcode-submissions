class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        flat = [x for row in grid for x in row]
        flat_set = set(flat)
        result = [0,0]
        count = Counter(flat)
        print(count)

        for i in range(1,len(grid)*len(grid) + 1):
            print(i)
            if i not in flat_set:
                result[1] = i
            elif count[i] == 2:
                result[0] = i


        return result
        

