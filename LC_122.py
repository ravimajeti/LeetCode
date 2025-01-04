class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in range(len(prices)-1):
            current_profit = prices[i+1] - prices[i]
            if current_profit > 0:
                max_profit += current_profit
        return max_profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(prices))
    prices = [1,2,3,4,5]
    print(solution.maxProfit(prices))
    prices.reverse()
    print(solution.maxProfit(prices))