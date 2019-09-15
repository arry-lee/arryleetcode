#完全平方数
#2019-01-14 15:46:46

class Solution:
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        def isSqr(n):
            a = int((math.sqrt(n)))
            return a * a == n
        
        dp = [0]*(n+1)
        dp[1] = 1
        
        for i in range(2,n+1):
            if isSqr(i):
                dp[i] = 1
            else:
                dp[i] = min([dp[j*j] + dp[i-j*j] for j in range(1,int(math.sqrt(i))+1)])
            
            # print(i,dp[i])
        return dp[n]        
                    
            