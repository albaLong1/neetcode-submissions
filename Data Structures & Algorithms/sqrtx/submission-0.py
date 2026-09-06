class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x
        res = l
        while l <= r:
            mid = (l + r) // 2
            product = mid * mid
            if product <= x:
                res = max(res, mid)
                l = mid + 1
            else:
                r = mid - 1
        return res