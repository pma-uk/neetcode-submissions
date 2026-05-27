class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        negStones = [-stone for stone in stones]
        heapq.heapify(negStones)

        while len(negStones) > 1:
            print(negStones)
            stone1 = heapq.heappop(negStones)
            stone2 = heapq.heappop(negStones)

            if stone1 == stone2:
                continue
            else:
                heapq.heappush(negStones, stone1 - stone2)

        if not negStones:
            return 0
        
        return -negStones[0]