import bisect

# O(log n)
class MySolution:
    def search(self, nums: list[int], target: int) -> int:
        N = len(nums)
        targetIndex = bisect.bisect_left(nums, target)
        if targetIndex < N and nums[targetIndex] == target:
            return targetIndex
        else :
            return -1

