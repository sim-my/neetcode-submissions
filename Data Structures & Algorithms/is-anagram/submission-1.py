class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = dict()
        t_map = dict()
        if(len(s) != len(t)):
            return False
        for x in s:
            if s_map.get(x) is not None:
                s_map[x] = s_map[x] + 1
            else:
                s_map[x] = 1

        for x in t:
            if t_map.get(x) is not None:
                t_map[x] = t_map[x] + 1
            else:
                t_map[x] = 1


        for s in s_map:
            if(t_map.get(s) is None):
                return False
            if(s_map[s] != t_map[s]):
                return False
        
        return True