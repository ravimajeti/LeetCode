class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_idx = 0
        max_profit = 0
        for i in range(1, len(prices)):
            new_max_profit = prices[i] - prices[buy_idx]
            if new_max_profit > max_profit:
                sell_idx = i
                max_profit = new_max_profit
            elif new_max_profit < 0:
                buy_idx = i
            else:
                pass
        return max_profit

if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit(prices))