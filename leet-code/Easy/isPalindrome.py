# Complexity: O(N)
# https://leetcode.com/problems/palindrome-number/submissions/1887351588
class MySolution:
    def isPalindrome(self, x: int) -> bool:
        strX = str(x)
        N = len(strX)
        isOdd = N % 2 != 0

        mid = N // 2
        first = strX[:mid]
        if isOdd:
            second = strX[mid+1:]
        else:
            second = strX[mid:]
        
        return first == second[::-1]

# O(log x)
class AdvanceSolution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes (e.g., -121 would be 121- reversed)
        if x < 0:
            return False

        # Initialize reverse to build the reversed number digit by digit
        reverse = 0
        # Store the original value of x to compare later (x will be modified in the loop)
        xcopy = x

        # Extract digits from right to left until all digits are processed
        while x > 0:
            # Build reversed number: shift existing digits left and add rightmost digit
            # Example: reverse=12, x=345 → reverse = (12*10) + (345%10) = 120 + 5 = 125
            reverse = (reverse * 10) + (x % 10)
            # Remove the rightmost digit from x (integer division by 10)
            # Example: x=345 → x = 345 // 10 = 34
            x //= 10

        # Compare the reversed number with the original value
        # If they are equal, the number is a palindrome
        return reverse == xcopy