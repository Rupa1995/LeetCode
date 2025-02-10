# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
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

# Function to print the linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Create linked list 1: 2 -> 4 -> 3
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

# Create linked list 2: 5 -> 6 -> 4
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

solution = Solution()  # Create an instance of the Solution class
result = solution.addTwoNumbers(l1, l2)  # Call the method


print_linked_list(result) # Print the result: 7 -> 0 -> 8 -> None


        