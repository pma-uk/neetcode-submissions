class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seenDict = {}

        for c in s:
            seenDict[c] = seenDict.get(c, 0) + 1

        for c in t:
            if c not in seenDict or seenDict[c] <= 0:
                return False
            
            seenDict[c] -= 1

        return True
