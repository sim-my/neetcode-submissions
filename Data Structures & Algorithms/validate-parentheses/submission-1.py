class Solution:
    def isValid(self, s: str) -> bool:
        if not s: return False
        stack = []
        pair = {')':'(', '}': '{', ']': '['}
        for letter in s:
            if stack and letter in pair and pair[letter] == stack[-1]:
                stack.pop()
            else:
                stack.append(letter)
        return len(stack) == 0