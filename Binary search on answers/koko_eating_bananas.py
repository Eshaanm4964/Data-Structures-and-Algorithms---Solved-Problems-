import math
class Solution:
    def CalcTotalHours(piles,speed):
        TotalHours = 0
        for bananas in piles:
            TotalHours += math.ceil(piles//speed)
        return TotalHours

    def min_speed(piles,h):
        max_pile = max(piles)
        low = 1
        high = max_pile
        while low <=high:
            mid = (low+high)//2
            TotalHours = self.CalcTotalHours(piles,mid)
            if TotalHours<h:
                ans = mid
                high = mid-1
            else:
                low = mid+1
        return ans 