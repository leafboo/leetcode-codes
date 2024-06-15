class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # if even number of len, immediately return
        if len(nums) % 2 == 0:
            return

        nums.sort()
        unique_num = nums[0]
        
        for i in range(1, len(nums) - 1, 2):
            if nums[i] != nums[i + 1]:
                unique_num = nums[i + 1]
        return unique_num
        