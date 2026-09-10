import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': lambda a, b: int(a / b),
        }

        for t in tokens:
            if t in operations:
                b = stack.pop()          # right operand — popped first
                a = stack.pop()          # left operand
                stack.append(operations[t](a, b))
            else:
                stack.append(int(t))

        return stack[0]