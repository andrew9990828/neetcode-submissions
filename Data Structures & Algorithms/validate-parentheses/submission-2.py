class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        stack = []

        for ch in s:
            if ch in pairs:
                if not stack:
                    return False
                else:
                    if stack[-1] != pairs[ch]:
                        return False
                    else:
                        stack.pop()
            else:
                stack.append(ch)
        
        return len(stack) == 0