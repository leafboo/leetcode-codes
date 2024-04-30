class Solution(object):
    def merge(self, nums1, m, nums2, n):
        left = []
        right = []

        for i in range(m):
            left.append(nums1[i])
        
        for i in range(n):
            right.append(nums2[i])

        # merge
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums1[k] = left[i]
                i += 1
            else:
                nums1[k] = right[j]
                j += 1
            k += 1

        while i < m:
            nums1[k] = left[i]
            i += 1
            k += 1
        while j < n:
            nums1[k] = right[j]
            j += 1
            k += 1
            


        