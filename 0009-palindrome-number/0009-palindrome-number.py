class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        convert = str(x)
        l = 0
        r = len(convert) - 1

        while (l < r):
            if convert[l] != convert[r]:
                return False
            l += 1
            r -= 1
        return True

        