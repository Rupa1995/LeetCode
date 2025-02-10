# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head
        
        while l1 or l2 or carry:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum_val = x + y + carry

            carry = sum_val // 10 # Calculate the new carry
            digit = sum_val % 10 # calculate digit to add 

            current.next = ListNode(digit) # Create a new node with the digit
            current = current.next

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next

        

        