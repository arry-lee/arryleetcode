#������
#2019-01-14 16:57:54

class Solution:
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        coins = [1] + nums + [1]
        n = len(coins)
        max_coins = [[0 for _ in range(n)] for _ in range(n)]
        
        for k in range(2, n):
            for left in range(n - k):
                right = left + k
                for i in range(left + 1, right):
                    max_coins[left][right] = max(max_coins[left][right], \
                           coins[left] * coins[i] * coins[right] + \
                           max_coins[left][i] + max_coins[i][right])
        return max_coins[0][-1]

