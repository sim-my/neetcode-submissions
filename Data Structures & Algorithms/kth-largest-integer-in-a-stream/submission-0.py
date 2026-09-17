class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        self.nums.append(val)
        s_nums = sorted(self.nums, reverse=True)
        print(s_nums)
        return s_nums[self.k-1] 
