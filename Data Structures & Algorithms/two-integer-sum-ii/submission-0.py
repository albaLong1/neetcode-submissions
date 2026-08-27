class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        left = 0
        right = len(numbers) - 1
        while left < right:
            sum_ans = numbers[left] + numbers[right]
            if ( sum_ans == target):
                left += 1
                right += 1
                ans.append(left)
                ans.append(right)
                break
            elif (sum_ans < target):
                left += 1
            else:
                right -= 1
        return ans
        