# 
# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/submissions/1891111230
class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        result = [False] * len(candies)
        for i, v in enumerate(candies):
            if v + extraCandies >= max(candies):
                result[i] = True

        return result
