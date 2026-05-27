class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t) or len(s) == 0 or len(t) == 0:
            return False

        charCountDict = {}

        for i in range(len(s)):
            charCountDict[s[i]] = charCountDict.get(s[i], 0) + 1
            charCountDict[t[i]] = charCountDict.get(t[i], 0) - 1

        for key, val in charCountDict.items():
            if val != 0:
                return False

        return True

