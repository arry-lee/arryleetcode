#¼ÓÒ»
#2019-08-12 21:17:31

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = -1
        try:
            while digits[i] == 9:
                digits[i] = 0
                i -= 1
            digits[i] += 1
        except IndexError:
            digits.insert(0,1)
       
        return digits