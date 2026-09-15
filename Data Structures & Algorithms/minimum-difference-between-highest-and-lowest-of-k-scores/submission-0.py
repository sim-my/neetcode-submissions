class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        best = float("inf")
        nums_sorted = sorted(nums)
        for right in range(k-1, len(nums_sorted)):
            best = min(best, nums_sorted[right] - nums_sorted[right - k + 1])

        return best