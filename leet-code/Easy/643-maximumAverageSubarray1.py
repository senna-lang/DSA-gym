# O(n)
# https://leetcode.com/problems/maximum-average-subarray-i/submissions/1900352403
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        N = len(nums)

        windowSum = sum(nums[:k])
        maxSum = windowSum
        for i in range(k, N):
            windowSum -= nums[i - k]
            windowSum += nums[i]
            maxSum = max(maxSum, windowSum)

        return maxSum / k