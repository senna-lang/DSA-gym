"""
Key Points
- By using a hash map, we can achieve O(n) time complexity.
- We store the values we have already scanned in a hash map as {value: index}.
- This allows us to look up a value and its index later in O(1) time.

When to Use a Hash Map
- When fast lookup or existence checking is required.
- When you need to access previously seen values inside a loop.
- When a mapping from values to information is needed (e.g., value → index).
- When the original order of the array matters and sorting is not allowed.

https://leetcode.com/problems/two-sum/submissions/1887336529
"""
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int] | None:
        seen = {}

        for i, x in enumerate(nums):
            need = target - x
            if need in seen:
                return [i, seen[need]]
            seen[x] = i
