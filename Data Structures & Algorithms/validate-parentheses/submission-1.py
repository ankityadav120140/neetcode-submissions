class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for i in s:
            if i in(['(','{',"["]):
                stack.append(i)
            else:
                if(len(stack) == 0):
                    return False
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                if i == '}' and stack[-1] == '{':
                    stack.pop()
                if i == ']' and stack[-1] == '[':
                    stack.pop()
        return len(stack) == 0