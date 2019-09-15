#×î´óÊı
#2018-11-07 13:51:49

class Solution(object):
    def largestNumber(self, nums):
        comp = lambda a, b: 1 if a + b > b + a else -1
        num_to_str = map(str, nums)
        num_to_str.sort(cmp=comp, reverse=True)
        return '0' if num_to_str[0] == '0' else ''.join(num_to_str)