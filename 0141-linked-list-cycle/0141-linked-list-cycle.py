# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        hash_set = set()

        while head:
            hash_set.add(head)
            head = head.next

            if head in hash_set:
                return True
        return False



       
        