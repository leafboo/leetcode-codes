class Solution(object):
    def specialArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        def binary_search(arr, val):
            l = 0
            r = len(arr) - 1

            while l <= r:
                m = (l + r) // 2
                if arr[m] < val:
                    l = m + 1
                else:
                    r = m - 1
            return l

        for i in range(1, len(nums) + 1):
            if len(nums) - binary_search(nums, i) == i:
                return i
        return -1


        