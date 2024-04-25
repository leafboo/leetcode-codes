class Solution(object):
    def longestCommonPrefix(self, strs):
        longest_prefix = ""
        shortest_word = min(strs, key=len)

        for i in range (len(shortest_word)):

          for j in range (len(strs) - 1):
              if strs[j][i] != strs[j + 1][i]:
                  return longest_prefix
          longest_prefix += strs[0][i]
        
        return longest_prefix

        

            