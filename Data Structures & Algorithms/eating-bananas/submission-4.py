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
            mid_rate = (l + r) // 2

            hours = get_hours(piles, mid_rate)  ## How long it takes at current rate

            if hours > h:
                ## Takes too long, rate not high enough
                l = mid_rate + 1
            else:
                ## Able to finish all bananas - record and make current rate new upper bound
                r = mid_rate - 1
                rate_k = mid_rate



        return rate_k

        