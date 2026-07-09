class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        initial = None
        profit = 0
        i = 0
        while i<len(prices)-1:
            if prices[i+1] >= prices[i]: #if next day >= current day
                if initial == None: #if no initial yet
                    initial = prices[i] 
                i += 1 #go to next day
                if i == len(prices)-1:
                    profit += (prices[i]-initial)
            elif prices[i+1]<= prices[i]: # if next day less than or equal to current day
                if initial == None:
                    i+=1
                else:
                    profit += (prices[i]-initial)
                    initial = None
                    i += 1

        return profit

