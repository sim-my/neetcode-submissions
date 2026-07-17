class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}  
        dict_t = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)} 

        for i in s:
            dict_s[i] = dict_s[i] + 1

        for j in t:
            dict_t[j] = dict_t[j] + 1


        result_s = "".join(str(v) for v in dict_s.values())
        result_t = "".join(str(w) for w in dict_t.values())


        if result_s == result_t:
            return True
        else:
            return False
