# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        headAlen, headBlen = 1, 1
        tempA, tempB = headA.next, headB.next

        # get length
        while tempA:
            tempA = tempA.next
            headAlen += 1
        while tempB:
            tempB = tempB.next
            headBlen += 1
        tempA, tempB = headA, headB

        # cut excess node/s
        while headAlen < headBlen:
            tempB = tempB.next
            headBlen -= 1
        while headAlen > headBlen:
            tempA = tempA.next
            headAlen -= 1

        # compare nodes
        for i in range(headAlen):
            if tempA == tempB:
                return tempA
            tempA = tempA.next
            tempB = tempB.next

        return None

        
    

         
        
        