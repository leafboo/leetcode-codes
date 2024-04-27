class Solution(object):
    def isValid(self, s):
        if len(s) % 2 != 0:
            return False

        closing = { "(": ")", "{": "}", "[": "]" }
        stack = []

        for char in s:
            if len(stack) > 0 and char == closing.get(stack[-1]):
                stack.pop()
                continue
            stack.append(char)

        if not stack:
            return True
        return False
            
        