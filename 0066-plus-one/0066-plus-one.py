class Solution(object):
    def plusOne(self, digits):
        num = len(digits) - 1
        isFinished = False
        toggle = False

        while digits[num] == 9:
            
            digits[num] = 0
            num -= 1
            toggle = True
           
         
        if digits[0] == 0 and toggle:
            return [1] + digits
        
        digits[num] += 1
        return digits
            
        