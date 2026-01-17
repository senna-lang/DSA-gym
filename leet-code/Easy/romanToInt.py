# O(n)
# https://leetcode.com/problems/roman-to-integer/submissions/1887761439
class MySolution:
    def romanToInt(self, s: str) -> int:
        dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        result = 0
        prev = 0

        for i in s:
            if dict[i] > prev:
                result += dict[i] - 2 * prev
            else:
                result += dict[i]
            
            prev = dict[i]

        return result

# O(n)
class AdvanceSolution:
    def romanToInt(self, s: str) -> int:
        # Initialize result counter to accumulate the integer value
        res = 0
        # Mapping of Roman numerals to their integer values
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        # Iterate through pairs of adjacent characters
        # zip(s, s[1:]) creates pairs: (s[0], s[1]), (s[1], s[2]), ... (s[n-2], s[n-1])
        # Example: "IV" → [('I', 'V')]
        #          "MCMXC" → [('M', 'C'), ('C', 'M'), ('M', 'X'), ('X', 'C')]
        for a, b in zip(s, s[1:]):
            # If current numeral value is less than next numeral, it's a subtractive case
            # Example: In "IV", 'I'(1) < 'V'(5), so we subtract 1 (later add 5)
            # Example: In "IX", 'I'(1) < 'X'(10), so we subtract 1 (later add 10)
            if roman[a] < roman[b]:
                res -= roman[a]
            else:
                # Otherwise, just add the current numeral value
                # Example: In "VI", 'V'(5) >= 'I'(1), so we add 5
                res += roman[a]

        # Add the last character's value (it's never a subtractive case)
        # The last numeral is always added because there's no next character to compare
        # Example: In "IV", we already processed 'I' and subtracted 1, now add 'V'(5) → result: 4
        #          In "MCMXC", we process pairs, then add 'C'(100) → result: 1990
        return res + roman[s[-1]] 