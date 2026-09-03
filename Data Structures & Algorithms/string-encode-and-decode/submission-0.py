class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for word in strs:
            string += f"{len(word)}" + "#" + word
        
        return string

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])

            # word begins after #
            word_start = j + 1
            word_end = word_start + length

            res.append(s[word_start:word_end])

            i = word_end

        return res