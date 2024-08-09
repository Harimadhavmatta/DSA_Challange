class Solution(object):
    def romanToInt(self, s):
        roman_numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        total = 0
        prev_value = 0
        s=s[::-1]
        print(s)
        for i in range(0,len(s)):
            current_value = roman_numerals[s[i]]
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            prev_value = current_value
        return total