#宝石与石头
#2019-08-17 06:20:13

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return len([stone for stone in S if stone in J])