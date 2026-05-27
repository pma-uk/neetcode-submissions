class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        seenCount = 0
        left, right = 0, 0

        s1Chars = {}

        for c in s1:
            s1Chars[c] = s1Chars.get(c,0) + 1

        while right < len(s2) and s2[right] not in s1Chars:
            right += 1
            left += 1
            
        while right < len(s2):
            c = s2[right]
            if c not in s1Chars:
                while left < right:
                    if s2[left] in s1Chars:
                        s1Chars[s2[left]] += 1
                        seenCount -= 1
                    left += 1
            elif s1Chars[c] == 0:
                while s1Chars[c] == 0:
                    s1Chars[s2[left]] += 1
                    seenCount -= 1
                    left += 1
                    
            if c in s1Chars:
                s1Chars[c] -= 1
                seenCount += 1

            print(f"{c}, {left}, {right}, {s1Chars}, {seenCount}")
            if seenCount == len(s1):
                return True

            right += 1
        return False
