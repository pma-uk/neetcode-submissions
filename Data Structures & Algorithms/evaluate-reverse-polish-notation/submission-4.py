class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operandStack = []

        for token in tokens:
            if token == "+":
                b = operandStack.pop()
                a = operandStack.pop()
                
                operandStack.append(a + b)
            elif token == "-":
                b = operandStack.pop()
                a = operandStack.pop()

                operandStack.append(a - b)
            elif token == "*":
                b = operandStack.pop()
                a = operandStack.pop()

                operandStack.append(a * b)
            elif token == "/":
                b = operandStack.pop()
                a = operandStack.pop()

                operandStack.append(int(a / b))
            else:
                operandStack.append(int(token))

        return operandStack[0]
                