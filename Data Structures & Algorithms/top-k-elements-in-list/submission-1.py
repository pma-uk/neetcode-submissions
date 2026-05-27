class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}


        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        thing = sorted(counts, key=counts.get, reverse=True)

        return thing[:k]