import math

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for c in tokens:
            if c.isdigit() or c.startswith('-') and c[1:].isdigit():
                stack.append(int(c))
            elif c in {"+", "-", "*", "/"}:
                op2 = stack.pop()
                op1 = stack.pop()
                if c == "+":
                    res = op1 + op2
                elif c == "-":
                    res = op1 - op2
                elif c == "*":
                    res = op1 * op2
                elif c == "/":
                    res = op1 / op2
                    if res >= 0:
                        res = int(math.floor(res))
                    else:
                        res = int(math.ceil(res)) 
                stack.append(res)
        return stack[0]