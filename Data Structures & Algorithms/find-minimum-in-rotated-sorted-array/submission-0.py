class Solution:
    def findMin(self, nums: List[int]) -> int:

        l,r = 0, len(nums) - 1

        minimum = 5001

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] < minimum:
                minimum = nums[mid]

            if nums[l] <= nums[r]:
                r = mid - 1
            else:
                if nums[mid] < nums[r]:
                    r = mid
                else:
                    l = mid + 1
        '''
        [3,4,5,1,2]
        [4,5,6,7,0,1,2]
        [9,2,4,6,7]
        [11,13,15,17]
        '''
        return minimum
        