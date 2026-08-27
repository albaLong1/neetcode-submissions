class Solution:
    import re
    def extract_chars(self, s: str) -> str:
        return re.sub(r'[^a-zA-Z0-9]','',s)
    
    def isPalindrome(self, s: str) -> bool:
        ans = self.extract_chars(s).lower()
        left = 0
        right = len(ans) - 1
        while left <= right:
            if ans[left] != ans[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
        