class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}

        for s in strs:
            chars = sorted(s)
            sorted_chars = "".join(chars)

            if sorted_chars in seen:
                seen[sorted_chars] += [s]
            else:
                seen[sorted_chars] = [s]
        
        res = []

        for val in seen.values():
            res.append(val)
        
        return res