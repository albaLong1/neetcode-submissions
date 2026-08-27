class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        answers = []
        while i <= len(nums) - 2:
            j = i + 1
            while j <= len(nums) - 1:
                sum = nums[i] + nums[j]
                if (sum == target):
                    answers.append(i)
                    answers.append(j)
                    return answers
                else:
                    j += 1
            i += 1
        return 