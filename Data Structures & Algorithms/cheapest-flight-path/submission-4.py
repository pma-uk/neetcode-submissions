class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        src_to_dst = defaultdict(list)

        for flight in flights:
            src_to_dst[flight[0]].append((flight[1], flight[2]))

        #flowest_cost = float('inf')
        min_heap = [(0, src, -1)] # (cost, source, number of stops)
        visited = {}

        # BFS
        while min_heap:
            prev_cost, curr_node, curr_stops = heapq.heappop(min_heap)
            
            if curr_node == dst:
                return prev_cost

            if curr_stops >= k:
                continue

            for next_node, curr_cost in src_to_dst[curr_node]:
                new_cost = prev_cost + curr_cost
                if (next_node, curr_stops + 1) not in visited or visited[(next_node, curr_stops + 1)] > new_cost:
                    visited[(next_node, curr_stops + 1)] = new_cost
                    heapq.heappush(min_heap, (new_cost, next_node, curr_stops + 1))

        
        # Path not found
        return -1