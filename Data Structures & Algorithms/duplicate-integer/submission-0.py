class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        collection = set()
        for x in nums:
            if(x in collection):
                return True
            collection.add(x)
        return False
