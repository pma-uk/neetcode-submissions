class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #closestK = heapq.nsmallest(k, points, key=lambda p: p[0]**2 + p[1]**2)
        
        minheap = []
        for point in points:
            dist = point[0]**2 + point[1]**2
            heapq.heappush(minheap, [dist, point[0], point[1]])

        #heapq.heapify(minheap)

        closestK = []

        for _ in range(k):
            point = heapq.heappop(minheap)
            closestK.append([point[1], point[2]])

        return closestK