#°´ÆæÅ¼ÅÅĞòÊı×é
#2019-07-30 23:02:14

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return sorted(A,key = lambda x:x&1)