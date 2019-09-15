#盈利计划
#2019-01-12 21:48:02

class Solution:

    def profitableSchemes(self, G, P, group, profit):
        MOD = 10**9 + 7
        cur = [[0] * (G + 1) for _ in range(P + 1)]
        cur[0][0] = 1

        for p0, g0 in zip(profit, group):
            # 每次添加一个新的犯罪
            # p0, g0 : the current crime profit and group size
            cur2 = [row[:] for row in cur]
            # 拷贝一份表格
            for p1 in range(P + 1):
                # 从第0行遍历到第P行，第p1行的利益为p1
                
                # p1 : the current profit
                # p2 : the new profit after committing this crime
                # 得到 p0 + p1 的利润，若大于P则只考虑P
                p2 = min(p1 + p0, P)
                
                for g1 in range(G - g0 + 1):
                    # g1在剩余人数中遍历
                    # g1 : the current group size
                    # g2 : the new group size after committing this crime
                    # g2是新的人数
                    g2 = g1 + g0
                    cur2[p2][g2] += cur[p1][g1]
                    cur2[p2][g2] %= MOD
            cur = cur2

        # Sum all schemes with profit P and group size 0 <= g <= G.
        return sum(cur[-1]) % MOD