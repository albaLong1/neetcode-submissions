class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        for element in operations:
            if element == "+":
                ans.append(ans[-1] + ans[-2])
            elif element == "D":
                ans.append(ans[-1] * 2)
            elif element == "C":
                ans.pop()
            else:
                ans.append(int(element))
        
        return sum(ans)