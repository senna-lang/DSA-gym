# O(n)
# https://leetcode.com/problems/max-consecutive-ones-iii/submissions/1903254540
class MySolution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        N = len(nums)
        wLeft = 0
        maxLen = 0
        remainK = k
        
        for i in range(N):
            if nums[i] == 0:
                remainK -= 1
            
            while remainK < 0:
                if nums[wLeft] == 0:
                    remainK += 1
                wLeft += 1
            
            maxLen = max(maxLen, i - wLeft + 1)
        
        return maxLen