# O(n)
# https://leetcode.com/problems/increasing-triplet-subsequence/submissions/1896350974
class Solution:
    def increasingTriplet(self, nums: list[int]) -> bool:
        a = float("inf")
        b = float("inf")

        for n in nums:
            if n <= a:
                a = n
            elif n <= b:
                b = n
            else:
                return True

        return False
