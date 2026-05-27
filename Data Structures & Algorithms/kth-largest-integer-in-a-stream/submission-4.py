import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # If we only care about the kth largest, keep only k values
        self.k = k
        self.topK = sorted(nums)[max(0, len(nums) - k):]
        heapq.heapify(self.topK)

    def add(self, val: int) -> int:
        if len(self.topK) != self.k:
            heapq.heappush(self.topK, val)
        elif val > min(self.topK):
            heapq.heapreplace(self.topK, val)
        return min(self.topK)
