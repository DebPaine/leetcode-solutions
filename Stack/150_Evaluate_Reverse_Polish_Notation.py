class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Time: O(n), where n is the len(tokens)
        Space: O(n), since we are using a stack
        """
        stack = []

        for token in tokens:
            if token == '+':
                a, b = stack.pop(), stack.pop()
                stack.append(b + a)
            elif token == '-':
                a, b = stack.pop(), stack.pop()
                stack.append(b - a)
            elif token == '*':
                a, b = stack.pop(), stack.pop()
                stack.append(b * a)
            elif token == '/':
                a, b = stack.pop(), stack.pop()
                # // won't work since for negative results it will give the next lowest negative number and won't
                # truncate towards zero. Also, int(string num) will return zero truncated value.
                stack.append(int(b / a))
            else:
                # If it's str(int)
                stack.append(int(token))

        return stack.pop()
