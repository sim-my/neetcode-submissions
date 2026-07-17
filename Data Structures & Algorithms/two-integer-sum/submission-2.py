class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i,x in enumerate(nums):
            val = target - x
            if val in my_dict:
                return [my_dict[val],i]
            my_dict[x] = i