#反转字符串中的元音字母
#2019-07-25 09:50:14

class Solution:
    def reverseVowels(self, s: str) -> str:
        v = 'aeiouAEIOU'
        s = list(s)
        l, r = 0, len(s)-1
        while l<r:
            if s[l] not in v:
                l += 1
            elif s[r] not in v:
                r -= 1
            else:
                s[l],s[r]=s[r],s[l]
                l += 1
                r -= 1
        return ''.join(s)