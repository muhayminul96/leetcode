class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

        total = 0
        prev_value = 0

        for char in reversed(s):  # Process from right to left
            value = roman_values[char]

            if value < prev_value:
                total -= value  # Subtraction case
            else:
                total += value  # Addition case

            prev_value = value

        return total



a = Solution()
a.romanToInt("III")