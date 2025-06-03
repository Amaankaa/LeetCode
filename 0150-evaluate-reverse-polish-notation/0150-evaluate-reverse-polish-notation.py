class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token not in ["+", "-", "*", "/"]:
                stack.append(int(token))
            else:
                val2 = stack.pop()  # Second operand
                val1 = stack.pop()  # First operand
                
                if token == "+":
                    stack.append(val1 + val2)
                elif token == "-":
                    stack.append(val1 - val2)
                elif token == "*":
                    stack.append(val1 * val2)
                else:  # Division
                    # Handle truncation toward zero
                    result = int(val1 / val2)
                    stack.append(result)
                    
        return stack[0]