# O(n)
# https://leetcode.com/problems/find-pivot-index/submissions/1905442472
class MySolution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        l = 0

        for i, n in enumerate(nums):
            if l == total - l - n:
                return i
            l += n

        return -1
