#验证回文串
#2019-08-13 00:59:50

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:return True
        s = ''.join([x.lower() for x in s if x.isalnum()])

        return s==s[::-1]