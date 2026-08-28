class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = l = 0
        length = r = len(height) - 1
        while length != 0:
            left = height[l]
            right = height[r]
            min_value = min(left, right)
            product = min_value * length
            if product > ans:
                ans = product
            if left > right:
                r -= 1
            else:
                l += 1
            length -= 1
        return ans
        