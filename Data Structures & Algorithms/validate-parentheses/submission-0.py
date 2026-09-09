class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")":
                if stack:
                    value = stack.pop()
                    if value != "(":
                        return False
                else:
                    return False
            elif char == "]":
                if stack:
                    value = stack.pop()
                    if value != "[":
                        return False
                else:
                    return False
            elif char == "}":
                if stack:
                    value = stack.pop()
                    if value != "{":
                        return False
                else:
                    return False
            
        if stack:
            return False
        else:
            return True
        