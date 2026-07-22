class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0
        nums_sorted = sorted(nums)
        for x in nums_sorted:
            prev_n = x
            x_set = set()
            x_set.add(x)
            for n in nums_sorted:
                if n == prev_n+1: 
                    x_set.add(n)
                    prev_n = n
            print(x_set)
            if len(x_set)> max_len: max_len = len(x_set)

        return max_len


