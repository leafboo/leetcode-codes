class Solution(object):
    def majorityElement(self, nums):
        recorded_nums = {}

        for num in nums:
            if num not in recorded_nums:
                recorded_nums[num] = 1
            else:
                recorded_nums[num] += 1

        max_key = max(recorded_nums, key=recorded_nums.get)
        return max_key


        