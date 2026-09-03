class Solution:

    def encode(self, strs: List[str]) -> str:

        concat_string = "".join(f"{len(s)}#{s}" for s in strs)

        return concat_string



    def decode(self, s: str) -> List[str]:
        #iterate from head=0 to str length:
        # find index of # by iterating j
        #difference between index of # and minus current index = 0
        #s[i:found(j) - i]
        # move head = j - i + 1
        # 
        #   1##
        head = 0
        result = []
        while head < len(s):  #while head < len(s):          
            j = s.index("#", head)     #j = s.index('#', head)           
            leng = int(s[head:j])  
            result.append(s[j+1: j+ 1+ leng])
            head = j + 1 + leng
            print(j, leng, head)
            
        return result



