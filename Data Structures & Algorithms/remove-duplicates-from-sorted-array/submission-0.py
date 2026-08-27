class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = 1
        left = right = 0
        while right < len(nums):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
                ans += 1
            right += 1
        return ans
        