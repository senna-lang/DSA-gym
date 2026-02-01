class MySolution:
    def maxVowels(self, s: str, k: int) -> int:
        N = len(s)
        maxVo = 0
        vowels = ["a", "i", "u", "e", "o"]

        for i in range(k):
            if s[i] in vowels:
                maxVo += 1

        windowVo = maxVo
        for i in range(k, N):
            if maxVo == k:
                return k
            if s[i] in vowels and s[i - k] not in vowels:
                windowVo += 1
            elif s[i] not in vowels and s[i - k] in vowels:
                windowVo -= 1
            maxVo = max(maxVo, windowVo)

        return maxVo
