class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        # Create a hashmap connecting each number to how many times it appears in nums
        dictionary = defaultdict(int)
        # Track the current frequency tier to target when adding to the answer
        t = 0
        # Count occurrences of each number and find the highest frequency
        for num in nums:
            dictionary[num] = 1 + dictionary.get(num, 0)
            if dictionary.get(num) > t:
                t = dictionary.get(num)

        # Keep adding numbers to the answer until it reaches length k
        while len(ans) < k:
            # Reset the next threshold each round so stale values don't carry over
            s = 0
            # Check every number in the dictionary
            for key in dictionary:
                # Skip numbers already added to the answer
                if key not in ans:
                    # Track the highest frequency strictly below t for the next round
                    if dictionary.get(key) < t and dictionary.get(key) > s:
                        s = dictionary.get(key)
                    # Add numbers whose frequency matches the current target
                    if dictionary.get(key) == t:
                        ans.append(key)
            # Lower the target to the next most frequent tier after the full loop finishes
            t = s
        return ans
            
        