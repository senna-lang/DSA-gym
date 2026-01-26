# O(n)
# https://leetcode.com/problems/string-compression/submissions/1897550060
class MySolution:
    def compress(self, chars: list[str]) -> int:
        N = len(chars)
        write = 0
        prev = chars[0]
        count = 1

        for i in range(1, N):
            if chars[i] == prev:
                count += 1
            else:
                chars[write] = prev
                write += 1
                if count > 1:
                    for d in str(count):
                        chars[write] = d
                        write += 1
                prev = chars[i]
                count = 1

        chars[write] = prev
        write += 1
        if count > 1:
            for d in str(count):
                chars[write] = d
                write += 1

        return write


class LeetCodeSolution:
    def compress(self, chars: list[str]) -> int:
        i = 0
        res = 0
        while i < len(chars):
            group_length = 1
            while (i + group_length < len(chars)
                   and chars[i + group_length] == chars[i]):
                group_length += 1
            chars[res] = chars[i]
            res += 1
            if group_length > 1:
                str_repr = str(group_length)
                chars[res:res+len(str_repr)] = list(str_repr)
                res += len(str_repr)
            i += group_length
        return res