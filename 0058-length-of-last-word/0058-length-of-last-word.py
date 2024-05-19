class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = 0
        for i in reversed(range(len(s))):
            if s[i] != ' ':
                counter += 1

            if counter > 0 and s[i] == ' ':
                return counter
        return counter
        
        