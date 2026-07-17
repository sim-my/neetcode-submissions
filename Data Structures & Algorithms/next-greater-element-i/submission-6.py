class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for x in nums1:
            index = nums2.index(x)
            found = False
            if(index == len(nums2) -1):
                output.append(-1)
            else:
                for i in range(index+1, len(nums2)):
                    if(nums2[i] > x):
                        output.append(nums2[i])   
                        found = True                    
                        break
                if not found:
                    output.append(-1)

        return output