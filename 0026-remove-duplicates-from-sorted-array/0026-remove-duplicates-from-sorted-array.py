class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        for r in range(1, len(nums)):
            if nums[l] == nums[r]:
                r += 1 
            else:
                nums[l + 1] = nums[r]
                l += 1
                
        return l + 1
            