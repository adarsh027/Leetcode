#Ref: https://www.youtube.com/watch?v=I7KXD2OGDRQ
# ref : https://www.youtube.com/watch?v=34WE6kwq49U
class Solution:
    def maxProfit(self, prices):
        cur_min = float('inf')
        max_profit = 0
        
        for i in range(len(prices)):
            cur_min  = min(cur_min, prices[i])
            profit = prices[i] - cur_min 
            max_profit = max(max_profit, profit)
            
        return max_profit

Solution().maxProfit([7,1,5,3,6,4])

# two pointer approach
#ref: https://www.youtube.com/watch?v=1pkOgXD63yU&list=PLot-Xpze53leOBgcVsJBEGrHPd_7x_koV&index=1
#ref: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/solutions/1735550/python-javascript-easy-solution-with-very-clear-explanation/
class Solution:
    def maxProfit(self, prices):
        max_profit= 0
        left=0 #represents buy
        right = 1 # represents sell
        while right<len(prices):
            cur_profit= prices[right]-prices[left]
            if cur_profit>0:
                max_profit= max(max_profit,cur_profit)
            else:
                left= right
            right+=1
        return max_profit
    
Solution().maxProfit([7,1,5,3,6,4])