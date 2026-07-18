class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mydict = {}
        for x in nums:
            if x in mydict:
                mydict[x] = mydict[x] + 1
            else:
                mydict[x] = 1


        sorted_dict_list = sorted(mydict, key=mydict.get, reverse=True)

        return sorted_dict_list[0:k]
   
        