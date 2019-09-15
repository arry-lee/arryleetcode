#最长公共前缀
#2019-08-13 01:58:47

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = ''
        for a in zip(*strs):
            print(a)
            if len(set(a))==1:
                s += a[0]
            else:
                break
        return s