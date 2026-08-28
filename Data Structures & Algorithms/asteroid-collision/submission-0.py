class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        ans = []
        for asteroid in asteroids:
            while len(ans) != 0 and asteroid < 0 and ans[-1] > 0:
                #TODO
                if abs(asteroid) > abs(ans[-1]):
                    ans.pop()
                elif abs(asteroid) < abs(ans[-1]):
                    break
                else:
                    ans.pop()
                    break
            else:
                ans.append(asteroid)
        return ans
        