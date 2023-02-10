# Definition for a singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val  # node value
        self.next = next  # reference to next node in the list

# Solution class to add two linked lists
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)  # create a dummy node and set cur equal to it
        carry = 0  # variable to keep track of the carry-over value
        while l1 or l2 or carry:  # while there are still nodes in l1 or l2 or a carry-over value
            if l1:
                carry += l1.val  # add the value of the current node in l1 to the carry-over value
                l1 = l1.next  # move to the next node in l1
            if l2:
                carry += l2.val  # add the value of the current node in l2 to the carry-over value
                l2 = l2.next  # move to the next node in l2
            cur.next = ListNode(carry % 10)  # create a new node with the current digit of the sum
            cur = cur.next  # move to the newly created node
            carry //= 10  # update the carry-over value for the next iteration
        return dummy.next  # return the next node after the dummy node (first actual node of the sum linked list)
