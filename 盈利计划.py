#ӯ���ƻ�
#2019-01-12 21:48:02

class Solution:

    def profitableSchemes(self, G, P, group, profit):
        MOD = 10**9 + 7
        cur = [[0] * (G + 1) for _ in range(P + 1)]
        cur[0][0] = 1

        for p0, g0 in zip(profit, group):
            # ÿ�����һ���µķ���
            # p0, g0 : the current crime profit and group size
            cur2 = [row[:] for row in cur]
            # ����һ�ݱ��
            for p1 in range(P + 1):
                # �ӵ�0�б�������P�У���p1�е�����Ϊp1
                
                # p1 : the current profit
                # p2 : the new profit after committing this crime
                # �õ� p0 + p1 ������������P��ֻ����P
                p2 = min(p1 + p0, P)
                
                for g1 in range(G - g0 + 1):
                    # g1��ʣ�������б���
                    # g1 : the current group size
                    # g2 : the new group size after committing this crime
                    # g2���µ�����
                    g2 = g1 + g0
                    cur2[p2][g2] += cur[p1][g1]
                    cur2[p2][g2] %= MOD
            cur = cur2

        # Sum all schemes with profit P and group size 0 <= g <= G.
        return sum(cur[-1]) % MOD