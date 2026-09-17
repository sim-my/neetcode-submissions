from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s2)
        k = len(s1)

        if k > n: return False
        count_s1 = Counter(s1)

        for right in range(k-1, n):
            left = right - k + 1
            count_s2 = Counter(s2[left:right+1])
            print(count_s1, count_s2, left, right)
            if count_s1 == count_s2:
                return True

        return False






            