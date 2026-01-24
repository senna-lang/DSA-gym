# O(n)
# https://leetcode.com/problems/reverse-words-in-a-string/submissions/1894850781
class MySolution:
    def reverseWords(self, s: str) -> str:
        words = []

        word = ""
        for c in s:
            if c.isspace():
                if word:
                    words.append(word)
                    word = ""
                    continue
                else:
                    continue

            word += c
        if word:
            words.append(word)

        words.reverse()

        return " ".join(words)

class AdvanceSolution:
    def reverseWords(self, s: str) -> str:
        # split() allows us to ignore leading, trailing, and multiple spaces
        words = s.split()
        res = []

        for i in range(len(words) - 1, -1, -1):
            res.append(words[i])
            if i != 0:
                res.append(" ")

        return "".join(res)