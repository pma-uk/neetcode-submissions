class Solution:
    def isValid(self, s: str) -> bool:
        bracketMap = {')': '(', '}': '{', ']': '['}
        openBracketStack = []

        for bracket in s:
            if bracket not in bracketMap:
                openBracketStack.append(bracket)
                continue
            
            if not openBracketStack or bracketMap[bracket] != openBracketStack.pop():
                return False
        
        return not openBracketStack
