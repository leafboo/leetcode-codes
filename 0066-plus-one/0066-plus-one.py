class Solution(object):
    def plusOne(self, digits):
        num = len(digits) - 1
        isFinished = False
        toggle = False

        while not isFinished:
            if digits[num] == 9:
                digits[num] = 0
                toggle = True
            elif digits[0] == 0 and toggle:
                isFinished = True
            else:
                digits[num] += 1
                return digits
            num -= 1
        return [1] + digits
            
        