#买卖股票的最佳时机II
#2019-08-12 20:41:04

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stack = []
        profit = 0
        for p in prices:
            if not stack:
                stack.append(p)
                
            elif p < stack[-1]:
                # 计算利润
                if len(stack)>1:
                    profit += stack[-1]-stack[0]                        
                stack.clear()
                stack.append(p)
            elif p > stack[-1]:
                stack.append(p)
        
        if stack:
            profit += stack[-1]-stack[0]
        return profit
                    