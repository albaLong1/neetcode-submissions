class Solution:

    def encode(self, strs):
        result = ""
        for s in strs:
            result += str(len(s)) + "#" + s  # e.g. "5#hello3#wow"
        return result

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":  # find the "#"
                j += 1
            length = int(s[i:j])  # number before "#"
            word = s[j+1 : j+1+length]  # grab exactly `length` chars after "#"
            result.append(word)
            i = j + 1 + length  # move i to the start of the next encoded word
        return result
