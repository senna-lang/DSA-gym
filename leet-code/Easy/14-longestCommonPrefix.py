# https://leetcode.com/problems/longest-common-prefix/submissions/1887798726
class MySolution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""

        for chars in zip(*strs):
            if len(set(chars)) == 1:
                prefix += chars[0]
            else:
                break

        return prefix
