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

        result = roman_numerals.get(s[0])

        for i in range (len(s) - 1):
            if (roman_numerals.get(s[i]) < roman_numerals.get(s[i + 1])):
                result += roman_numerals.get(s[i + 1]) - (roman_numerals.get(s[i]) * 2)
            else :
                result += roman_numerals.get(s[i + 1])
   
        return result
                
        

        # first step: loop through the given roman numerals
        # check if the current rn is less than the next rn
        # individual solution for both cases

