from collections import defaultdict, Counter
from itertools import zip_longest

# O(n)
# https://leetcode.com/problems/determine-if-two-strings-are-close/submissions/1907941748
class MySolution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        memoA = defaultdict(int)
        memoB = defaultdict(int)

        if set(word1) != set(word2):
            return False

        for a, b in zip_longest(word1, word2):
            memoA[a] += 1
            memoB[b] += 1

        valuesA = memoA.values()
        valuesB = memoB.values()

        return sorted(valuesA) == sorted(valuesB)



class AdvanceSolution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if set(word1) != set(word2):
            return False

        return sorted(Counter(word1).values()) == \
               sorted(Counter(word2).values())
