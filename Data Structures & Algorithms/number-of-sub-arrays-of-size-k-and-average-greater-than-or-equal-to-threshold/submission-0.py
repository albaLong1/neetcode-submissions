class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        total = 0
        l = 0
        for r in range( len(arr)):
            if r - l >= k:
                total -= arr[l]
                l += 1
            total += arr[r]
            if (r + 1) >= k:
                average = total / k
                if average >= threshold:
                    ans += 1
        return ans
        
        