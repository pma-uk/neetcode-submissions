class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        currMax = 1
        

        index = 0

        # Do it character by character
        # Slide window once out of the # of max possible chars
        while index < len(s):
            currChar = s[index]
            currLength = 0
            kCounter = k
            nextIndex = -1

            # Move index and count length while duplicates found or k remaining chars
            while index < len(s) and kCounter >= 0:
                if s[index] != currChar:
                    if kCounter == 0:
                        break
                    # Next character index found
                    if kCounter == k:
                        nextIndex = index
                    kCounter -= 1
                index += 1
                currLength += 1

            # If kCounter remaining, then add to length if possible
            if kCounter > 0:
                currLength = min(currLength + kCounter, len(s))

            currMax = max(currMax, currLength)

            if nextIndex != -1:
                index = nextIndex
             

        return currMax