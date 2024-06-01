# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return head

        pointer = head
        checker = pointer.next

        while checker:
            if checker.val != pointer.val:
                pointer.next = checker
                pointer = checker
            elif checker.next == None:
                pointer.next = checker.next
            checker = checker.next
        return head
        