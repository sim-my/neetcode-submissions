class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 
       
        s_count = Counter(s)
        t_count = Counter(t)

        for x in s_count:
            if x not in t_count:
                return False
            if t_count[x] != s_count[x]:
                return False

        return True
