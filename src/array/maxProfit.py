#买卖股票的最佳时机 II
#===============================================================================
# 输入: [7,1,5,3,6,4]
# 输出: 7
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
# 随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。
#===============================================================================
#贪心算法，总是做出在当前看来是最好的选择，不从整体最优上加以考虑，也就是说，只关心当前最优解
#当今天的价格比前一天的价格高，也就是利润>0,那么就进行一笔交易。能赚一笔是一笔，苍蝇再小也是肉嘛
class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit=0
        for i in range(len(prices)-1):
            if(prices[i+1]>prices[i]):
                max_profit+=(prices[i+1]-prices[i])
        return max_profit
    
if __name__ == '__main__':
    prices=[7,1,5,3,6,4]
    max_profit=Solution().maxProfit(prices)
    print(max_profit)