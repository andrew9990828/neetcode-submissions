class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Monotonic stack problem
        # Strore indexs waiting for a warmer day
        stack = []
        res = [0] * len(temperatures)

        for i, tmp in enumerate(temperatures):
            if not stack:
                stack.append(i)
            else:
                while stack and temperatures[stack[-1]] < tmp:
                    idx = stack.pop()
                    res[idx] = i - idx
                else:
                    stack.append(i)

        return res