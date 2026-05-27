class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        charCounts = defaultdict(int)
        maxLength = 0
        
        left = 0
        longest = 0 # Length of longest substring in s so far

        for right, c in enumerate(s):
            charCounts[c] += 1
            longest = max(longest, charCounts[c])

            while (right - left + 1) - longest > k:
                # Triggers when either
                #  1) more than k replacements for current substring
                #  2) longest no longer increasing
                #     i.e., longest controls window size
                #     and only increases if longer substring found
                charCounts[s[left]] -= 1
                left += 1
            maxLength = max(maxLength, right - left + 1)

        return maxLength
