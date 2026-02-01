# 0(n)
# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/submissions/1903916750
class MySolution:
    def longestSubarray(self, nums: list[int]) -> int:
        N = len(nums)
        wLeft = 0
        longest = 0

        delete = False
        for i in range(N):
            if nums[i] == 0:
                if delete:
                    while delete:
                        if nums[wLeft] == 0:
                            delete = False
                        wLeft += 1
                delete = True

            longest = max(longest, i - wLeft)

        return longest


class AdvanceSolution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)

        left = 0
        zeros = 0
        ans = 0

        for right in range(n):
            if nums[right] == 0:
                zeros += 1

            while zeros > 1:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            ans = max(ans, right - left + 1 - zeros)

        return ans - 1 if ans == n else ans