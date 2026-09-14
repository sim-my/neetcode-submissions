class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = Counter(blocks[0:k])
        best = count['W']
        left = 0

        for right in range(k, len(blocks)):
            count[blocks[right]] += 1
            count[blocks[left]] -= 1
            left+=1
            if count['W'] + count['B'] == k:
                best = min(best, count['W'])

        return best


            