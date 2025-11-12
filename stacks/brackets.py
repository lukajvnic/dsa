class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        pairs = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        opens = list("({[")
        closes = list(")}]")

        for char in s:
            if char in opens:
                stack.append(char)
            elif char in closes:
                if len(stack) == 0:
                    return False
                top = stack.pop()
                if pairs[char] != top:
                    return False
            else:
                return False
        
        return len(stack) == 0


sol = Solution()
print(sol.isValid("[]"))
