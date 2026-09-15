class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = list(s)
        verification = set()
        l = 0
        length = 0
        for r in range(len(chars)):
            while chars[r] in verification:
                verification.discard(chars[l])
                l += 1
            verification.add(chars[r])
            length = max(len(verification), length)
        
        return length
        