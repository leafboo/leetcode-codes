class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        num = len(digits) - 1
        isFinished = False
        toggle = False

        while not isFinished and digits[num] != 0:
            if digits[num] + 1 > 9:
                digits[num] = 0
                num -= 1
                toggle = True
            else:
                digits[num] += 1
                isFinished = True
         
        if digits[0] == 0 and toggle:
            return [1] + digits
        elif digits[num] == 0:
            digits[num] += 1
        return digits
            
        