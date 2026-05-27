class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        tokenStack = []

        for token in tokens:

            if token == '+':
                a, b = tokenStack.pop(), tokenStack.pop()
                tokenStack.append(b + a)
            elif token == "-":
                a, b = tokenStack.pop(), tokenStack.pop()
                tokenStack.append(b - a)
            elif token == "*":
                a, b = tokenStack.pop(), tokenStack.pop()
                tokenStack.append(b * a)
            elif token == "/":
                a, b = tokenStack.pop(), tokenStack.pop()
                tokenStack.append(int(float(b) / a))
            else:
                tokenStack.append(int(token))
        
        return tokenStack[0]