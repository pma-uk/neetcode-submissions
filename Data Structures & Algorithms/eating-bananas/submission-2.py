class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hours(piles, rate):
            hours = 0

            for pile in piles:
                hours += math.ceil(pile/rate)

            return hours
        ## Upper bound eating rate is the max of piles
        ## Lower bound is 1

        ## If h == length of piles, eating rate must be max of piles
        ## eating rate is monotonically decreasing as h increases.

        ## Treat as binary search problem, looking for rate between 1 and max(piles)
        l, r = 1, max(piles)

        if h == len(piles):
            return r

        rate_k = r

        while l <= r:
            mid = (l + r) // 2

            hours = get_hours(piles, mid)

            if hours > h:
                ## Takes too long, rate not high enough
                l = mid + 1
            else:
                r = mid - 1
                rate_k = min(rate_k, mid)



        return rate_k

        