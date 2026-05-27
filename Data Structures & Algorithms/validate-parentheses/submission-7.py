class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {")":"(", "]":"[", "}":"{"}
        openStack = []

        for c in s:
            if c in brackets:
                if not openStack or brackets[c] != openStack.pop():
                    return False
            else:
                openStack.append(c)
        
        if openStack:
            return False
        return True