class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        k = nums[0]
        longest = 1
        memory = defaultdict(int)
        for num in nums:
            if num in memory:
                memory[num] += 1
                length = memory.get(num)
                if length > longest:
                    k = num
                    longest = length
            else:
                memory[num] = 1
        return k
        