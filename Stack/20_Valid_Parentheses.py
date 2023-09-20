class Solution:
    def isValid(self, s: str) -> bool:
        """
        Time: O(n), where n if len(s)
        Space: O(n), since we are using a stack
        """
        complement = {')': '(', ']': '[', '}': '{'}
        stack = []

        for i, char in enumerate(s):
            # If char is an opening bracket
            if char not in complement:
                stack.append(char)
            # If stack is not empty and top of stack has opening bracket
            elif stack and stack[-1] == complement[char]:
                stack.pop()
            else:
                return False

        # If stack still has opening bracket but we have iterated through entire string
        if stack:
            return False

        return True
