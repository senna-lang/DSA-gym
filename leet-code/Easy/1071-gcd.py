# O(Min(Len(Str1),Len(Str2)))
# https://leetcode.com/problems/greatest-common-divisor-of-strings/submissions/1891067277
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Ensure both strings have the same repeating structure
        if str1 + str2 != str2 + str1:
            return ""

        def gcd(lenA, lenB):
            minLen = min(lenA, lenB)
            for i in range(minLen, 0, -1):
                # Determine the length of the GCD string
                if lenA % i == 0 and lenB % i == 0:
                    return i
            return 1

        return str1[: gcd(len(str1), len(str2))]
