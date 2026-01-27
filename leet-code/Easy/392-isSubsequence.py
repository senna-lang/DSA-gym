# O(n)
# https://leetcode.com/problems/is-subsequence/submissions/1898499944
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        N = len(s)
        p = 0

        if not s:
            return True

        for c in t:
            if c == s[p]:
                if p == N - 1:
                    return True
                p += 1
        
        return False 
        
# with Two Pointer
class AdvanceSolution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sp = tp = 0

        while sp < len(s) and tp < len(t):
            if s[sp] == t[tp]:
                sp += 1
            tp += 1
        
        return sp == len(s)