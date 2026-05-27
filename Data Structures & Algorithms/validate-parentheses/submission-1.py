class Solution:
    def isValid(self, s: str) -> bool:
        def checkBracketMatch(left: str, right: str) -> bool:
            if left == '[' and right == ']':
                return True
            if left == '(' and right == ')':
                return True
            if left == '{' and right == '}':
                return True
            return False

        if len(s) % 2 != 0:
            return False

        bracketStack = []

        for bracket in s:
            if bracket in "([{":
                bracketStack.append(bracket)
                continue
            
            if not bracketStack:
                return False

            bracketToClose = bracketStack.pop()

            if not checkBracketMatch(bracketToClose, bracket):
                return False

        if bracketStack:
            return False

        return True