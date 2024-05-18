class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range (len(haystack)):
            for j in range(len(needle)):
                if i + j >= len(haystack):
                    return -1
                elif needle [j] != haystack[i + j]:
                    break
                elif j + 1 == len(needle):
                    return i
        return -1
        