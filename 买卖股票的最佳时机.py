#������Ʊ�����ʱ��
#2019-08-13 04:31:19

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # �ֽ�
        minprice = float('inf')
        maxprofit = 0
        
        for price in prices:
            if price < minprice:
                minprice = price
            if price > minprice:
                maxprofit = max(price-minprice,maxprofit)
        return maxprofit