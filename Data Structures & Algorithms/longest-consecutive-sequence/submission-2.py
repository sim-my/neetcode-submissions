class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        arr = sorted(set(nums))
        max_len = len_items = 1
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1] + 1:
                len_items = len_items + 1
            else:
                len_items = 1

            max_len = max(max_len, len_items)
        return max_len
