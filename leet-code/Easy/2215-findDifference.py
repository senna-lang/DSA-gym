# O(n)
# https://leetcode.com/problems/find-the-difference-of-two-arrays/submissions/1907904665
class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        setA = set(nums1)
        setB = set(nums2)

        return [list(setA - setB), list(setB - setA)]
