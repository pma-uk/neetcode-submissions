class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestLength = 0
        seenDict = {}

        startIndex = 0
        for endIndex, c in enumerate(s):
            # If character already seen, and its index is at/past current start of substring
            # we've got a duplicate
            if c in seenDict and seenDict[c] >= startIndex:
                # Move start of new substring to the right of old duplicate
                startIndex = seenDict[c] + 1
            
            # Get longest length, accounting for missing +1, e.g., single character
            longestLength = max(longestLength, endIndex - startIndex + 1)
            seenDict[c] = endIndex

        return longestLength
            
                

