class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return nums
        
        rotation = k % len(nums)
        index = 0
        while index < rotation:
            index += 1
            value = nums.pop()
            nums.insert(0,value)