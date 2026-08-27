class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = []
        measure = len(nums) // 3
        memory = defaultdict(int)
        for num in nums:
            memory[num] = memory.get(num,0) + 1
            length = memory.get(num)
            if length > measure:
                if num not in ans:
                    ans.append(num)
        return ans
        