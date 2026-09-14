class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = Counter(blocks[0:k])
        best = count['W']
        left = 0

        for right in range(k, len(blocks)):
            left+=1
            count = Counter(blocks[left:right+1])

            print(blocks[left:right], count['W'], count['B'])
            if count['W'] + count['B'] == k:
                best = min(best, count['W'])

        return best


            