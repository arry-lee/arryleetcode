#��ת�ַ�����ĵ���
#2019-07-25 23:06:15

class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.strip().split()
        l.reverse()
        print(l)
        return ' '.join(l)