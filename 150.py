import math


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token.isdigit() or (token[0] == "-") and token[1:].isdigit():
                stack.append(token)
            else:
                second_num = stack.pop()
                first_num = stack.pop()

                stack.append(math.trunc(eval(f"{first_num}{token}{second_num}")))

        return int(stack[0])
