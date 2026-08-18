class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = collections.deque()

        for token in tokens:
            if token in "+-*/":
                n1 = stack.pop()
                n2 = stack.pop()

                if token == "+":
                    res = n2 + n1
                elif token == "-":
                    res = n2 - n1
                elif token == "*":
                    res = n2 * n1
                else:
                    res = int(n2 / n1)

                stack.append(res)
            else:
                stack.append(int(token))

        return stack.pop()