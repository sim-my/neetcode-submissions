class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r = 0, len(nums) - 1
        while l<r:
            k = (l+r) // 2
        
            if nums[k] > nums[r]:
                l = k + 1
            else:
                r = k
        
        pivot =  l


        if target >=nums[pivot] and target <= nums[n-1]:
            l,r = pivot, n-1
        else:
            l,r = 0, pivot - 1


        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                r = mid-1
            else:
                l = mid+1

        
        return -1