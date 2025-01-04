class Solution(object):
    def maxProfit_forLoop(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_idx = 0
        max_profit = 0
        for i in range(1, len(prices)):
            new_max_profit = prices[i] - prices[buy_idx]
            if new_max_profit > max_profit:
                max_profit = new_max_profit
            elif new_max_profit < 0:
                buy_idx = i
            else:
                pass
        return max_profit
    
    def maxProfit_whileLoop(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_ptr = 0
        max_profit = 0
        sell_ptr = 1
        while sell_ptr < len(prices):
            current_profit = prices[sell_ptr] - prices[buy_ptr]
            if current_profit < 0:
                buy_ptr = sell_ptr
            elif current_profit > max_profit:
                max_profit = current_profit
            elif current_profit < max_profit:
                pass
            sell_ptr += 1
        return max_profit


if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    solution = Solution()
    print(solution.maxProfit_forLoop(prices))
    print(solution.maxProfit_whileLoop(prices))