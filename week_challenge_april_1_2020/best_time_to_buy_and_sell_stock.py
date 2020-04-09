from typing import List

# https://leetcode.com/submissions/detail/321903708/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        current_buying_price = None
        for current_end, current_price in enumerate(prices):
            if current_buying_price == None:
                current_buying_price = current_price
                current_selling_price = current_price
            else:
                if current_price < current_buying_price or current_selling_price > current_price:
                    # Set new starter, add previous if complete to total profit
                    profit = current_selling_price - current_buying_price
                    if profit > 0:
                        total_profit += profit
                    current_buying_price = current_price
                    current_selling_price = current_price
                elif current_selling_price < current_price:
                    # set a new end of range
                    current_selling_price = current_price
        profit = current_selling_price - current_buying_price
        if profit > 0:
            total_profit += profit
        return total_profit

        # [7,1,5,3,4,6], Profit = 7
        # [7,1,5,3,6,4], Profit = 7
        # [1,2,3,4,5], Profit = 4
        # [7,6,4,3,1], Profit = 0
        '''
        for current_end, current_price in enumerate(prices):
            if current_profit <= 0:
                current_start = current_end
                current_profit = current_price
            else:
                if current_price - nums[current_start] > current_profit:
                    pass

            if current_profit > best_profit and current_start != current_end:
                best_start = 0
                best_end = current_end
                best_profit = current_profit
        '''

        '''
        for current_end, current_price in enumerate(prices):
            if current_profit == None:
                current_start = current_end
                current_selling_price = price
                current_profit = 0
            else:
                if prices[current_start] > current_price and current_profit <= 0:
                    current_start = current_end
                    current_selling_price = price
                    current_profit = 0
                elif prices[current_start] < current_price and \
                    current_selling_price - prices[current_start] > current_profit:
                    current_profit = current_selling_price - prices[current_start]
                    current_
        '''

if __name__ == '__main__':
    obj = Solution()
    #data = [7,1,5,3,6,4]
    #data = [7,1,5,3,4,6]
    #data = [1,2,3,4,5]
    #data = [7,6,4,3,1]
    profit = obj.maxProfit(data)
    print(str(profit))
