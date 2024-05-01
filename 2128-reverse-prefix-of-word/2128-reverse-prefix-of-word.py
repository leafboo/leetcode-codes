class Solution(object):
    def reversePrefix(self, word, ch):
        array_word = list(word)
        index = None
        for i in range(len(array_word)):
            if array_word[i] == ch:
                index = i
                break
            elif i == len(array_word):
                return
  
        # swap
        l = 0
        r = index

        while l < r:
            store_char = array_word[l]
            array_word[l] = array_word[r]
            array_word[r] = store_char

            l += 1
            r -= 1
        return ''.join(array_word)

