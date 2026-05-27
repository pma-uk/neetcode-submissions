class Solution:
    def getCharCount(self, s: str):
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord("a")] += 1
        
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramDict = defaultdict(list)

        for s in strs:
            anagramDict[self.getCharCount(s)].append(s)

        return anagramDict.values()

