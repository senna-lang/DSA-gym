from collections import defaultdict

# O(n)
# https://leetcode.com/problems/unique-number-of-occurrences/submissions/1907916949
class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        memo = {}

        for n in arr:
            if n not in memo:
                memo[n] = 1
            else :
                memo[n] += 1
        
        values = memo.values()

        return len(values) == len(set(values))
        

class AdvanceSolution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        memo = defaultdict(int)

        for n in arr:
            memo[n] += 1

        return len(memo.values()) == len(set(memo.values()))