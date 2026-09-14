class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = Counter(blocks[0:k])
        best = count['W']

        for right in range(k, len(blocks)):
            count[blocks[right]] += 1
            count[blocks[right-k]] -= 1
            best = min(best, count['W'])

        return best


            