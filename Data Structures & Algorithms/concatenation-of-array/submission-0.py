class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        length = 0
        while length < 2:
            index = 0
            while index < len(nums):
                ans.append(nums[index])
                index +=1
            length += 1
        return ans
        