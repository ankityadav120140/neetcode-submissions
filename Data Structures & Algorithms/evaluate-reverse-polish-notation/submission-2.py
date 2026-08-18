class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = ["+", "-", "*", "/"]
        stack = collections.deque()

        for ch in tokens:
            if ch in ops:
                n1 = stack.pop()
                n2 = stack.pop()
                res = 0
                if(ch == "+"):
                    res = n1 + n2
                elif ch == "-":
                    res = n2 - n1
                elif ch == "*":
                    res = n2 * n1
                elif ch == "/":
                    res = n2 // n1
                print(res)
                
                stack.append(res)

            else:
                stack.append(int(ch))
        return stack.pop()