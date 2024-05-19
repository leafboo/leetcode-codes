class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        arr = []

        for i in range(len(nums)):
            if nums[i] != val:
                arr.append(nums[i])
        nums[:] = arr
        

        