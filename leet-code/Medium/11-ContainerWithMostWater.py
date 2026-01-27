# O(n)
# https://leetcode.com/problems/container-with-most-water/submissions/1898599592
class MySolution:
    def maxArea(self, height: list[int]) -> int:
        N = len(height)
        l = 0
        r = N - 1

        maxM = 0

        while l < r:
            w = r - l
            m = min(height[l], height[r]) * w
            if maxM < m:
                maxM = m
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return maxM