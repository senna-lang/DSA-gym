# https://leetcode.com/problems/valid-parentheses/submissions/1888512465
class MySolution:
    def isValid(self, s: str) -> bool:
        parDict = {"}": "{", ")": "(", "]": "["}
        leftPar = ["{", "(", "["]
        left = []

        for i in s:
            if i in leftPar:
                left.append(i)
            else:
                if len(left) != 0 and left[-1] == parDict[i]:
                    left.pop()
                    continue
                else:
                    return False

        return len(left) == 0
        
class AdvancedSolution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
        
        return not stack