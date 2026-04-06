class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []

        for t in tokens:
            if t not in '+-*/':
                operands.append(int(t))
            else:
                operand2 = operands.pop()
                operand1 = operands.pop()

                if t == '+':
                    operands.append(operand1 + operand2)
                elif t == '-':
                    operands.append(operand1 - operand2)
                elif t == '*':
                    operands.append(operand1 * operand2)
                elif t == '/':
                    operands.append(int(operand1 / operand2))
        
        return operands[0]
        