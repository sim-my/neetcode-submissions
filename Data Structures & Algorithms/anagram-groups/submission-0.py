class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #result dictionary
        result = defaultdict(list)
        #first loop - word
        for str in strs:    
            count = [0]*26
            #second loop - each letter
            for s in str:
                count[ord(s) - ord("a")] = count[ord(s) - ord("a")] + 1

            result[tuple(count)].append(str)


        return list(result.values())