class Solution:

    def encode(self, strs: List[str]) -> str:

        concat_string = "".join(f"{len(s)}#{s}" for s in strs)

        return concat_string



    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != '#':
                j = j + 1
            len_str = int(s[i:j])
            val = s[j+1: j+1+len_str]
            res.append(val)
            i =  j+1+len_str

        return res

