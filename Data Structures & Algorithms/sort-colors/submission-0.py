class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeroes = nums.count(0)
        ones = nums.count(1)
        twos = nums.count(2)
        list_zero = [0] * zeroes
        list_one = [1] * ones
        list_two = [2] * twos
        combined = list_zero + list_one + list_two
        nums[:] = combined
        