class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        ans = nums[:len(nums)]
        ans.sort()
        i = 1
        while i < len(nums):
            if ans[i-1] == ans[i]:
                return ans[i]
            i +=1
        