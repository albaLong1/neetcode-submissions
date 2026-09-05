class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #1,2,3,4,5,6,7,8,9,10
        l= max(weights)
        r = sum(weights) 

        res = r 
        while l <= r:
            capacity = (l + r) // 2
            limit = 0
            daysPassed = 0
            for weight in weights:
                if (limit + weight) > capacity:
                    daysPassed += 1
                    limit = 0 
                    limit += weight
                else:
                    limit += weight
            
            daysPassed += 1

            if daysPassed <= days:
                res = min(capacity,r)
                r = capacity - 1
            else:
                l = capacity + 1
        
        return res
        