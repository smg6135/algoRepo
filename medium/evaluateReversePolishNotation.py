from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        else:
            op = tokens.pop()
            right, left = 0, 0
            if tokens[-1].strip("-").isnumeric():
                right = int(tokens.pop())
                left = self.evalRPN(tokens)
            else:
                left = int(tokens[0])
                right = self.evalRPN(tokens[1:])

            match op:
                case "+":
                    return left + right
                case "-":
                    return left - right
                case "*":
                    return left * right
                case "/":
                    return left / right
                case other:
                    return 0

print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))