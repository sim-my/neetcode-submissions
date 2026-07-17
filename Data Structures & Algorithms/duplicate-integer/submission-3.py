class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = {}
        for item in nums:
            if item in mydict:
                return True
            else:
                mydict[item] = 1
        return False
