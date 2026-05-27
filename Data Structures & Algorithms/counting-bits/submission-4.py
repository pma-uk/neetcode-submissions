class Solution:
    def countBits(self, n: int) -> List[int]:
        results = [0]
        offset = 1

        for i in range(1, n+1):
            if offset * 2 == i:
                offset = i
            
            results.append(results[i-offset] + 1)

        return results
